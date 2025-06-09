def check_three_digits(list_n):
    list_r = []
    for num in list_n:
        if num in range(100,1000):
            list_r.append(num)
    print(list_r)
    if len(list_r) > 0:
        return True
    return False


print(check_three_digits([12,54,692,563,7777]))