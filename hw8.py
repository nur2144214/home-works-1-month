program_attempts = []
print("Загадайте число от 1 до 100")


def save_results(user_num):
    with open("results.txt", "w", encoding='utf-8') as file:
        file.write(f"попытки: {program_attempts}\nколичество попыток: "
                   f"{len(program_attempts)}\nзагаданное число: {user_num}")


def search_num(attempts: str, low: int, high: int):
    guess = (low + high) // 2
    if attempts == ">" or attempts.lower() == "больше":
        low = guess + 1
        program_attempts.append(guess)
    elif attempts == '<' or attempts.lower() == 'меньше':
        high = guess - 1
        program_attempts.append(guess)
    elif attempts == 'равно' or attempts == '=':
        program_attempts.append(guess)
        save_results(guess)
        return "равно", low, high
    else:
        print("неправильный ввод;")
        return None, low, high
    return guess, low, high


low = 1
high = 100
guess = (low + high) // 2
while True:
    print("вводите только: > (больше), < (меньше), = (равно)")
    answer_division = input(f"ваше число {guess}?: ")
    result, low, high = search_num(answer_division, low, high)
    if result == "равно":
        print(f"число угадано, результаты в файле results.txt")
        break
    elif result is not None:
        guess = (low + high) // 2
