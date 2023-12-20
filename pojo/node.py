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
        # 使用{{和}}表示普通的大括号
        serviceInfo = ", ".join(str(service) for service in self.serviceList)
        return f"nodeName:{self.name}, serviceList:{{ {serviceInfo} }}"
