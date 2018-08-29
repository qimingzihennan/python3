from sys import argv, path

print('================python from import===================================')
print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path
for i in argv:
    print(i)
