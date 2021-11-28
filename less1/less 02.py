test_01 = int(input("Введите любое время в секундах: "))
if test_01 < 60:
    print(f"Время (c): {test_01:02}")
elif int(test_01) < 3600:
    print(f"Время (м:c): {test_01 // 60:02}: {test_01 % 60:02}")
else:
    print(f"Время (ч:м:c): {test_01 // 3600:02}:{(test_01 % 3600) // 60:02}:{test_01 % 60:02}")