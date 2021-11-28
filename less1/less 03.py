test_01 = int(input("Введите число: "))
test_02 = 0
while test_01 >0:
    if test_01 % 10 > test_02:
        test_02 = test_01 % 10
        if test_02 == 9:
            break
    test_01 //= 10
print(f"Наибольшая цифра: {test_02}")