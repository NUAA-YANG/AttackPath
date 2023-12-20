"""
@Author：YZX
@Date：2023/12/20 16:13
@Python：3.9
"""


# 节点类
class Node:
    # 包含节点名称和节点拥有的服务列表
    def __init__(self, name, serviceList):
        self.name = name
        self.serviceList = serviceList

    def __str__(self):
        return f"name:{self.name}, serviceList:{self.serviceList}"