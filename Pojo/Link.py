"""
@Author：YZX
@Date：2023/12/8 16:26
@Python：3.9
"""

# 描述链路性能
class Link:
    def __init__(self, name, bandwidth, delay):
        self.name = name
        self.bandwidth = bandwidth
        self.delay = delay

    def __str__(self):
        return f"name:{self.name}, bandwidth:{self.bandwidth}, delay:{self.delay}"
