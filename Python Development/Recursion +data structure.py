def natural_number(number):
    if number<=0:
        return[]
    else:
        return natural_number(number-1)+[number]
result=natural_number(5)
print(f"natural number is {result}")


def count_digits(Lst):
    if len(Lst)==0:
        return 0
    else:
        return 1+ count_digits(Lst[1:])
result=count_digits([1,2,3,4,5])
print(f"count_digits : {result}")


