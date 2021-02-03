# from rp_01_测试模块1 import say_hello
from rp_02_测试模块2 import say_hello as module2_say_hello
from rp_01_测试模块1 import say_hello

# 从不同的模块中导入相同的函数时, 后倒入的函数会覆盖前一个函数
module2_say_hello()
say_hello()
