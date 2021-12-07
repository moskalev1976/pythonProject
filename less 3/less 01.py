def div_nums(a, b):
    if b == 0:
        return "Нельзя делить на ноль!"
    else:
        return a / b
a = float(input("a: "))
b = float(input("b: "))
print(div_nums(a, b))
