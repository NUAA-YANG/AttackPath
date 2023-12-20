"""
@Author：YZX
@Date：2023/12/8 15:12
@Python：3.9
"""
import torch
from net import Net
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt


# 构建DQN网络
class DQN:
    # 状态、动作、经验池大小、学习率、奖励程度、贪婪选择概率、随机抽取经验数量
    def __init__(self, states, actions, memorySize, learningRate, gamma, eGreedy, reloadTargetIter, batchSize):
        # 状态空间：[节点名称，节点运行服务列表{service1, service1}]
        # 当前只记录最多3个服务，不满3个，则补充为""
        self.states = states
        # 动作空间：[攻击节点名称，攻击节点服务名称]
        self.actions = actions
        # 经验池大小
        self.memorySize = memorySize
        # 学习率
        self.learningRate = learningRate
        # 奖励程度
        self.gamma = gamma
        # 贪婪选择概率
        self.eGreedy = eGreedy
        # 每走多少步，更新一次target网络
        self.reloadTargetIter = reloadTargetIter
        # 从样本数据经验池中随机获得多少组经验
        self.batchSize = batchSize

        # 创建一个eval网络，计算当前状态下的 Q 值，估计当前策略的质量
        self.evalNet = Net(states, actions)
        # 创建一个target网络，计算目标 Q 值，提供一个相对稳定的目标值
        self.targetNet = Net(states, actions)
        # 损失函数
        self.loss = nn.MSELoss()
        # 优化器
        self.optimizer = torch.optim.Adam(self.evalNet.parameters(), lr=self.learningRate)
        # 创建记忆矩阵：当前节点名称+攻击节点名称+选择攻击的服务+奖励+下一个状态
        self.memory = np.zeros((self.memorySize, 1 + 1 + 1 + 1 + 1))
        # 记录学习总步数，每选择一个动作就加 1，用作整除reloadTargetIter，更新target网络
        self.learnStepCount = 0
        # 记录当前指向数据库第几个数据
        self.memoryCount = 0
        # 记录损失值
        self.cost = []
        # 记录每轮走的步数
        self.eachEpisodeStep = []

    # 动作选择
    def chooseAction(self, state):
        # 扩展一行,因为网络是多维矩阵,输入是至少两维
        state = torch.unsqueeze(torch.FloatTensor(state), 0)
        if np.random.uniform() < self.eGreedy:
            # 获取动作对应的值集合
            actionList = self.evalNet.forward(state)
            # 取值最大的值表示的动作
            action = torch.max(actionList, 1)[1].data.numpy()[0]
        else:
            # 随机选择动作
            action = np.random.randint(0, self.actions)
        return action

    # 存储学习经验，包括当前节点的名称，攻击节点的名称，攻击节点服务，奖励，下一个状态
    def storeMemory(self, currentNode, attackNode, attackService, reward, nextNode):
        # nodeName、nextNodeName、attackService为字符串、reward为整型
        # 为保证数据类型一致，全部转化为集合，以np类型捆绑经验存储
        transition = np.hstack((currentNode, attackNode, attackService, [reward], nextNode))
        # index 是 这一次录入的数据在 MEMORY_CAPACITY 的哪一个位置
        index = self.memoryCount % self.memorySize
        # 如果记忆超过上线，我们重新索引，即覆盖老的记忆
        self.memory[index, :] = transition
        # 经验池加一
        self.memoryCount += 1

    # 训练：evalNet是每次learn就进行更新，targetNet是达到次数后更新
    def learn(self):
        # 更新targetNet，每循环多少次就更新一下
        if self.learnStepCount % self.reloadTargetIter == 0:
            self.targetNet.load_state_dict((self.evalNet.state_dict()))
        self.learnStepCount += 1
        # 经验池已满，随机抽取batchSize个数据组成一维数组进行学习
        if self.memoryCount > self.memorySize:
            sampleIndex = np.random.choice(self.memorySize, self.batchSize)
        else:
            # 经验池未满，从现有的经验中随机抽取
            sampleIndex = np.random.choice(self.memoryCount, self.batchSize)
        # 按照随机获得的索引值获取对应的记忆数据
        memory = self.memory[sampleIndex, :]
        # 从记忆当中获取[0,1)列，即第一列，表示状态特征
        state = torch.FloatTensor(memory[:, :1])
        # 从记忆当中获取[1,3)列，即第二、三列，表示动作特征
        action = torch.FloatTensor(memory[:, 1:3])
        # 从记忆当中获取[3,4)列，即第四列，表示奖励特征
        reward = torch.FloatTensor(memory[:, 3:4])
        # 从记忆当中获取[4,5)列，即第五列，表示下一状态特征
        nextState = torch.FloatTensor(memory[:, 4:5])

        # 根据当前的状态输出动作Q值
        qEval = self.evalNet.forward(state).gather(1, action)
        # 根据下一步的状态，获取其中Q值最大的
        qNext = self.targetNet.forward(nextState).detach()
        # 计算qTarget
        qTarget = reward + self.gamma * qNext.max(1)[0].unsqueeze(1)
        # 计算损失值
        loss = self.loss(qEval, qTarget)
        # 记录损失值
        self.cost.append(loss.detach().numpy())
        # 梯度重置
        self.optimizer.zero_grad()
        # 反向求导
        loss.backward()
        # 更新模型参数
        self.optimizer.step()

    # 绘制损失图
    def drawCostImage(self):
        plt.plot(np.arange(len(self.cost)), self.cost)
        plt.xlabel("step")
        plt.ylabel("cost")
        plt.show()

