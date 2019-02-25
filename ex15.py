count = 0
num1 = 0
while True:
    num = int(input("データ入力(負の数で終了)>"))
    if num < 0:
        break


    num1 += num
    count += 1
    ave = num1/count
print("データ数:",count, "合計:",num1,"平均:",ave)
