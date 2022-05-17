# Задание номер 1
name = input("Введите свое имя: ")
password = input("Введите свой пароль: ")
age = input("Введите свой возраст: ")

print("Ваши данные для входа в аккаунт: имя - ", name, "," " пароль - ", password, "," " возраст - ", age)




# Задание номер 2

time = int(input("Вводите время в секундах: "))

hours = time / 3600
hours_second = hours * 60

minutes = time / 60

seconds = time

print("Время в формате ч:м:с - ", hours, ":", minutes, ":", seconds)




# Задание номер 3

number = int(input("Введите число n: "))

second_part = number + number
third_part = number + number + number

summy = number + second_part + third_part
print(summy)



# Задание номер 4

number = int(input("Введите число положительное число: "))
r = -1
while number > 10:
    d = number % 10
    number //= 10
    if d > r:
        r = d
print("Самая большая цифра в числе: ", r)


# Задание номер 5

money = int(input("Введите выручку фирмы: "))
taxes = int(input("Введите издержки фирмы: "))

if money != taxes:
    summy = money - taxes
    print("Финансовый результат - прибыль. Ее величина: ", summy)

profitability = summy / money
print("Рентабельность выручки = ", profitability)

empoyee = int(input("Введите численность сотрудников фирмы: "))
result = summy / empoyee

print("Прибыль фирмы в расчете на одного сотрудника: ", result)



# Задание номер 6

a = int(input("Введите результат первого дня: "))
b = int(input("Введите километраж: "))
day = 1

while a < b:
    a = a + (a * 0.1)
    day += 1
print("на ", day, "-й день  спортсмен достиг результата — не менее ", b, "км")



