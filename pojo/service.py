"""
@Author：YZX
@Date：2023/12/8 16:13
@Python：3.9
"""


# 服务类，描述每个节点上运行的服务
class Service:
    # 包含服务名称、服务攻击代价、服务攻击成功概率
    # 常见被攻击服务：{web,sql,ssh,mail,samba,vsftpd,dns,vpn}
    def __init__(self, name, complexity, needInteraction, confidentiality, probability):
        # 服务名称
        self.name = name
        # 服务复杂性：{low medium high}
        self.complexity = complexity
        # 是否需要交互：{yes no}
        self.needInteraction = needInteraction
        # 机密性：{low medium high}
        self.confidentiality = confidentiality
        # 被攻陷概率：{0-1}
        self.probability = probability

    # 输出
    def __str__(self):
        return f"[serviceName:{self.name},complexity:{self.complexity},complexity:{self.needInteraction}," \
               f"complexity:{self.confidentiality},probability:{self.probability}]"