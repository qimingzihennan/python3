from abstest import *


def main_test():
    print("main_test")


listArray = ['html', 'js', 'css', 'python']
for abc in listArray:
    my_test(abc)
print("=============")
i = 0
while i < 5:
    my_test(i)
    i = i + 1
my_abs(0.2)
print("=============")
for bc in listArray:
    my_test(bc)
    my_abs(0.2)
print("=============")
my_abs(0.2)
main_test()

print("=============")
returnTest = returnTest("测试");
print(returnTest)
