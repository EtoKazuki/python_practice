year = int(input("年>"))
month = int(input("月>"))
day = int(input("日>"))
weekday = (year + (year // 4) - (year // 100) + (year // 400) + ((13*month+8) // 5) + day) % 7
if weekday == 0:
    weekday = "日曜日"
elif weekday == 1:
    weekday = "月曜日"
elif weekday == 2:
    weekday = "火曜日"
elif weekday == 3:
    weekday = "水曜日"
elif weekday == 4:
    weekday = "木曜日"
elif weekday == 5:
    weekday = "金曜日"
elif weekday == 6:
    weekday = "土曜日"

if month == 13:
    month = month%12
    year = year+1
elif month == 14:
    month = month%12
    year = year+1

print(year,"年",month,"月",day,"日は",weekday,"です。")
