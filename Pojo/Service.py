"""
@Author：YZX
@Date：2023/12/8 16:13
@Python：3.9
"""

# 服务类，描述每个节点上运行的服务
class Service:
    # 包含服务名称、服务攻击代价、服务攻击成功概率
    # 常见被攻击服务：{web,sql,ssh,mail,file,dns,vpn,ntp}
    def __init__(self, name, cost, probability):
        self.name = name
        self.cost = cost
        self.probability = probability

    def __str__(self):
        return f"name:{self.name}, cost:{self.cost}, probability:{self.probability}"
