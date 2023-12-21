"""
@Author：YZX
@Date：2023/12/20 16:13
@Python：3.9
"""

from service import Service

# 节点类
class Node:
    # 包含节点名称和节点拥有的服务列表
    def __init__(self, name, serviceList):
        self.name = name
        self.serviceList = serviceList

    def strNodeService(self):
        # 使用{{和}}表示普通的大括号
        serviceInfo = ", ".join(Service.strService(ser) for ser in self.serviceList)
        return f"nodeName:{self.name}, serviceList:{{ {serviceInfo} }}"

    def strNodeScore(self):
        # 使用{{和}}表示普通的大括号
        serviceInfo = ", ".join(Service.strScore(service) for service in self.serviceList)
        return f"nodeName:{self.name}, serviceList:{{ {serviceInfo} }}"
