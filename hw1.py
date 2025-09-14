monday = float(input("Введите расходы за понедельник: "))
tuesday = float(input("Введите расходы за вторник: "))
wednesday = float(input("Введите расходы за среду: "))
thursday = float(input("Введите расходы за четверг: "))
friday = float(input("Введите расходы за пятницу: "))
saturday = float(input("Введите расходы за субботу: "))
sunday = float(input("Введите расходы за воскресенье: "))

week_sum = monday + tuesday + wednesday + thursday + friday + thursday + friday + saturday + sunday
average_consuption = week_sum / 7


print(f"общая сумма расходов: {week_sum}, средний расход за день: {round(average_consuption, 1)}")