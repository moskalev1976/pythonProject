def user_info(name, surname, year, city, email, phone):
    return f'{name} {surname} {year} {city} {email} {phone}'

n = input("Имя: ")
s = input("Фамилия: ")
y = input("Год: ")
c = input("Город: ")
e = input("E-mail: ")
p = input("Телефон: ")
result = user_info(name=n, surname=s, year=y, city=c, email=e, phone=p)
print(result)
