import os

os.system("shutdown /s")
string = "我是大傻狗"
hide_string = "我要走后门"
print("您的电脑将在1分钟后关机")
inputs = input(f"输入:【{string}】,则取消注销关机")
if inputs == string or inputs == hide_string:
    os.system("shutdown -a")
else:
    input("???????不听话?准备接受审判把")
