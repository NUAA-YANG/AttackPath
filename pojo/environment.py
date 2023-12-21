"""
@Author：YZX
@Date：2023/12/20 16:03
@Python：3.9
"""
from pojo.node import Node
from build import handle


# 描述当前网络环境
class Environment:
    def __init__(self, stateNodes, src, dst, linkList):
        # 节点列表
        self.stateNodes = stateNodes
        # 源节点
        self.src = src
        # 目的节点
        self.dst = dst
        # 链路信息
        self.linkList = linkList


if __name__ == '__main__':
    web = handle.normalizeService(handle.getServiceByName("web"))
    samba = handle.normalizeService(handle.getServiceByName("samba"))
    vpn = handle.normalizeService(handle.getServiceByName("vpn"))
    R1 = Node("R1", {web, samba, vpn})
    print(R1.strNodeScore())
    print(R1.strNodeService())


