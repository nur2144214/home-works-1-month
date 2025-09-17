# январь,
#  февраль,
#  март,
#  апрель,
#  май,
#  июнь,
#  июль,
#  август,
#  сентябрь,
#  октябрь,
#  ноябрь,
#  декабрь.

day = int(input("введите день рождения: "))
month = int(input("введите месяц рождения: "))

if day < 1 or day > 31 or month > 12 or month < 1:
    print("не правильно введенная дата")
elif day > 28 and month == 2:
    print("не правильно введенная дата")
elif (month == 4 or month == 6 or month == 9 or month == 11) and day > 30:
    print("не правильно введенная дата")


elif (month == 3 and day >= 21) or (month == 4 and day <= 20):
    print("вы Овен")
elif (month == 4 and day >= 21) or (month == 5 and day <= 21):
    print("вы Телец")
elif (month == 5 and day >= 22) or (month == 6 and day <= 21):
    print("вы Близнецы")
elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
    print("вы Рак")
elif (month == 7 and day >= 23) or (month == 8 and day <= 21):
    print("вы Лев")
elif (month == 8 and day >= 22) or (month == 9 and day <= 23):
    print("вы Дева")
elif (month == 9 and day >= 24) or (month == 10 and day <= 23):
    print("вы Весы")
elif (month == 10 and day >= 24) or (month == 11 and day <= 22):
    print("вы Скорпион")
elif (month == 11 and day >= 23) or (month == 12 and day <= 22):
    print("вы Стрелец")
elif (month == 12 and day >= 23) or (month == 1 and day <= 20):
    print("вы Козерог")
elif (month == 1 and day >= 21) or (month == 2 and day <= 19):
    print("вы Водолей")
elif (month == 2 and day >= 20) or (month == 3 and day <= 20):
    print("вы Рыба")