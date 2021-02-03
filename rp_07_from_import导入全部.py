from rp_01_测试模块1 import *
from rp_02_测试模块2 import say_hello
# 不推荐使用from...import *
# 因为出现重名的时候难以排查

say_hello()
dog = Dog()
print(dog)