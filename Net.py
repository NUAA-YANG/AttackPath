"""
@Author：YZX
@Date：2023/12/8 10:05
@Python：3.9
"""
import torch.nn as nn
import torch.nn.functional as F


# 用于构建深度神经网络
class MyNet(nn.Module):
    def __init__(self, states, actions):
        super(MyNet, self).__init__()
        # 创建一个线形层
        self.f1 = nn.Linear(states, 64)
        # 创建第二个线性层
        self.f2 = nn.Linear(64, 128)
        # 创建一个输出层
        self.softmax = nn.Linear(128, actions)
        # 初始化随机生成权重，范围是0-0.1
        self.f1.weight.data.normal_(0, 0.1)
        self.f2.weight.data.normal_(0, 0.1)
        self.softmax.weight.data.normal_(0, 0.1)
        # 激活函数
        self.relu = nn.ReLU()

    # 预测动作的值
    def forward(self, state):
        # 第一步：线性-激活
        state = self.relu(self.f1(state))
        # 第二步：线性-激活
        state = self.relu(self.f1(state))
        # 第三步 Dropout：随机地将输入中50%的神经元激活设为0，即去掉了一些神经节点，防止过拟合
        state = F.dropout(state, p=0.5)
        # 第四步：全连接输出
        out = self.softmax(state)
        return out
