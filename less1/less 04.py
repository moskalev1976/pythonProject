test_01 = int(input("Выручка: "))
test_02 = int(input("Издержки: "))

if test_02 > test_01:
    print("Убыток!")
else:
    print("Прибыль!")
    test_03 = (test_01-test_02) / test_01
    print(f"Рентабильность: {test_03}")
    test_04 = int(input("Количество штатных сотрудников: "))
    test_05 = (test_01 - test_02) / test_04
    print(f"Прибыль в расчете на одного сотрудника: {test_05}")