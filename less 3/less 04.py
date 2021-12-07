def get_pow(x, y):
    if x < 0:
        return 'X должно быть больше 0'
    if y > 0:
        return 'Y должно быть меньше 0'
    z = 1
    for i in range(y * -1):
        z *= x
    return 1 / z
x = float(input("Пожалуйста введите положительное число (X): "))
y = int(input("Пожалуйста введите отрицательное целое число (Y): "))
print(get_pow(x, y))
