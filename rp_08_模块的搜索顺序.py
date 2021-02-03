import random

rand = random.randint(0, 10)

print(rand)
# 自定义模块切忌和系统的模块重名

print(random.__file__)
