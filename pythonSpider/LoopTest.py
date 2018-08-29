# names = ['Michael', 'Bob', 'Tracy']
# print("names长度：" + str(len(names)))
# i = 0
# for name in names:
#     print("name:" + name)
# i = i + 1
# print(i)

if __name__ == '__main__':
    listArray = ['html', 'js', 'css', 'python']

    # 方法1
    print
    '遍历列表方法1：'
    for i in listArray:
        print("序号：%s   值：%s" % (listArray.index(i) + 1, i))
print("==========1")

print
'\n遍历列表方法2：'
# 方法2
for j in range(len(listArray)):
    print("序号：%s   值：%s" % (j + 1, listArray[j]))
print("==========2")
# 方法3
print
'\n遍历列表方法3：'
for k, val in enumerate(listArray):
    print("序号：%s   值：%s" % (k + 1, val))

print("==========3")
# 方法3
print
'\n遍历列表方法3 （设置遍历开始初始位置，只改变了起始序号）：'
for l, val in enumerate(listArray, 2):
    print("序号：%s   值：%s" % (l + 1, val))
