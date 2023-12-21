"""
@Author：YZX
@Date：2023/12/20 20:29
@Python：3.9
"""
from pojo.service import Service


# 归一化函数
def normalization(value, valueMax, valueMin):
    if valueMax == valueMin:
        return 0
    return (value - valueMin) / (valueMax - valueMin)


# 为服务设置分数
def normalizeService(service):
    # 复杂程度越低越好
    complexityMap = {"low": 0.9, "medium": 0.7, "high": 0.4}
    # 无需交互更好
    needInteractionMap = {"yes": 0.9, "no": 0.6}
    # 机密性越高越好
    confidentialityMap = {"low": 0.4, "medium": 0.7, "high": 0.9}
    # 赋值得分
    service.score = round(complexityMap.get(service.complexity, 0) + needInteractionMap.get(service.needInteraction, 0) + confidentialityMap.get(service.confidentiality, 0),2)
    return service


# 获取需要运行的服务
def getServiceByName(name):
    if name == "web":
        # 网络服务器
        return Service(name="web", complexity="medium", needInteraction="yes", confidentiality="high",
                       probability=0.7)
    elif name == "sql":
        # 数据库
        return Service(name="sql", complexity="medium", needInteraction="yes", confidentiality="high",
                       probability=0.6)
    elif name == "ssh":
        # 远程访问和管理
        return Service(name="ssh", complexity="medium", needInteraction="yes", confidentiality="high",
                       probability=0.9)
    elif name == "mail":
        # 邮件
        return Service(name="mail", complexity="medium", needInteraction="no", confidentiality="high",
                       probability=0.5)
    elif name == "samba":
        # 文件共享
        return Service(name="samba", complexity="medium", needInteraction="no", confidentiality="medium",
                       probability=0.6)
    elif name == "vsftpd":
        # tfp文件存储服务器
        return Service(name="vsftpd", complexity="low", needInteraction="no", confidentiality="low",
                       probability=0.4)
    elif name == "dns":
        # 域名服务
        return Service(name="dns", complexity="medium", needInteraction="no", confidentiality="medium",
                       probability=0.5)
    elif name == "vpn":
        # 虚拟专用网
        return Service(name="vpn", complexity="high", needInteraction="yes", confidentiality="high",
                       probability=0.8)
    else:
        return None


# 归一化处理链路参数
def normalizeLink(linkList):
    # 用于记录链路的值
    linkMap = {}
    # 链路的带宽最小值和最大值
    bandwidthMax = linkList[0].bandwidth
    bandwidthMin = linkList[0].bandwidth
    # 链路的时延最大值和最小值
    delayMax = linkList[0].delay
    delayMin = linkList[0].delay
    # 遍历链路集合，获取整个链路中的带宽和时延极值
    for link in linkList:
        bandwidthMax = max(bandwidthMax, link.bandwidth)
        bandwidthMin = min(bandwidthMin, link.bandwidth)
        delayMax = max(delayMax, link.delay)
        delayMin = min(delayMin, link.delay)
    # 开始归一化处理链路属性值
    for link in linkList:
        link.bandwidth = normalization(link.bandwidth, bandwidthMax, bandwidthMin)
        link.delay = normalization(link.delay, delayMax, delayMin)
        # 带宽越大越好，时延越小越好，所以相减
        linkMap[link.name] = link.bandwidth - link.delay
    # 返回归一化处理后的链路表和链路键值对
    return linkList, linkMap



