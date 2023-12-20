"""
@Author：YZX
@Date：2023/12/20 16:03
@Python：3.9
"""
from pojo.node import Node
from pojo.service import Service


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
