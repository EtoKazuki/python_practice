money = int(input("金額(円)>"))
print("金額:",money)
if 10000 < money:
    hoge = money // 10000
    money = money - 10000*hoge
    print("一万円札=",hoge,"枚")
if 5000 < money:
    hoge = money // 5000
    money = money - 5000*hoge
    print("五千円札=",hoge,"枚")
if 1000 < money:
    hoge = money // 1000
    money = money - 1000*hoge
    print("千円札=",hoge,"枚")
if 500 < money:
    hoge = money // 500
    money = money - 500*hoge
    print("五百円玉=",hoge,"枚")
if 100 < money:
    hoge = money // 100
    money = money - 100*hoge
    print("百円玉=",hoge,"枚")
if 50 < money:
    hoge = money // 50
    money = money - 50*hoge
    print("五十円玉=",hoge,"枚")
if 10 < money:
    hoge = money // 10
    money = money - 10*hoge
    print("十円玉=",hoge,"枚")
if 5 < money:
    hoge = money // 5
    money = money - 5*hoge
    print("五円玉=",hoge,"枚")
if 5 > money:
    print("一円玉=",money,"枚")
