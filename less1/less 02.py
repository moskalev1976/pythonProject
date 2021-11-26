test_01 = input("Введите любое время в секундах: ")
test_02 = int(test_01)/60
print(f"Время (ч:м) \n {int(test_02)}:{int(round(test_02%1,2)*60)}")