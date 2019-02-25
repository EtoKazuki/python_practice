num1 = int(input("数1>"))
num2 = int(input("数2>"))
num3 = int(input("数3>"))

if num1 > num2:
    hoge = num1
    num1 = num2
    num2 = hoge

if num1 > num3:
    hoge = num1
    num1 = num3
    num3 = hoge

if num2 > num3:
    hoge = num2
    num2 = num3
    num3 = hoge


print(num1,num2,num3,sep = ' ')
