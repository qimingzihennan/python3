print("Hello, World!")
if True:
    print("This is true")
else:
    print("This is false")
item_one = 123
total = item_one + \
        item_one + \
        item_one
print(total)

word = '字符串'
sentence = "这是一个句子"
paragraph = """这是一个段落，可以邮多行组成"""
print(word+sentence+paragraph)
str='Runoob'

print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第五个的字符
print(str[2:])             # 输出从第三个开始的后的所有字符
print(str * 2)             # 输出字符串两次
print(str + '你好')        # 连接字符串

print('------------------------------')

print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符

print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
print('------------------------------')
testString = 'testString'
print("testString："+testString)
testString="dafdfasdfsaf"
print("testString："+testString)