def security_is(password):
    if len(password) < 6:
        return False

    special = 0
    digit = 0
    upper = 0
    lower = 0

    for i in password:
        if not i.isalnum():
            special += 1
        if i.isdigit():
            digit += 1
        if i.isupper():
            upper += 1
        if i.islower():
            lower += 1

    if special >= 2 and digit > 0 and upper > 0 and lower > 0:
        return True
    else:
        return False


def nearest_num(lst, num = 0):
        if not lst:
            return None
        return min(lst, key=lambda x: abs(x - num))

print(nearest_num([3, 5, 6, 1]))