def nearest_num(lst, num):
    if not lst:
        return None
    ans = min(lst, key=lambda x: abs(x - num))
    end_lst = sorted(lst, key=lambda x: abs(x - num))
    return (ans, end_lst)

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)


def print_by_index(lst: list):
    while True:
        user_input = input("Введите индекс или 'выход': ")
        if user_input.lower() == 'выход':
            break
        try:
            get_obj = int(user_input)
            print(lst[get_obj])
        except IndexError:
            lenlist = len(lst) - 1
            print(f"вводите только возможные индексы 0 - {lenlist}")
        except ValueError:
            print('ошибка')

print_by_index([5, 2, 1, 5])