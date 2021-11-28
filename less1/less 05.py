test_01 = float(input("Дистанция в первый день: "))
test_02 = float(input("Цель: "))
test_03 = 1
while test_01 < test_02:
    test_01 *= 1.1
    test_03 +=1
print(f"Нужное число дней - {test_03}")