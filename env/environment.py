"""
@Author：YZX
@Date：2023/12/20 16:03
@Python：3.9
"""


# 描述当前网络环境
class Environment:
    def __init__(self, state, src, dst, links):
        # 节点列表
        self.state = state
        # 源节点
        self.src = src
        # 目的节点
        self.dst = dst
        # 链路信息
        self.links = links

# if __name__ == '__main__':
# Service1 = Service("samba", 500, 0.8)
# Service2 = Service("sql", 400, 0.5)
# R1 = Node("R1", [Service1, Service2])
