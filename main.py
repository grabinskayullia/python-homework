# Задание №1

our_f = open('practice.txt', 'w', encoding='utf-8')
line = input("Введите информацию: ")

while True:
    our_f.writelines(line)
    line = input("Введите информацию: ")
    if not line:
        break

our_f.close()
our_f = open('practice.txt', 'r')
content = our_f.readline()
print(content)
our_f.close()

# Задание №2
file = open("task2.txt", encoding="utf-8")

lines = 0
words = 0

for line in file:
    lines += 1
    words += len(line.split())

print(f"Колчество срок: {lines}")
print(f"Колчество слов: {words}")

file.close()

# Задание №3
with open("task3.txt", 'r', encoding="utf-8") as file:
    workers = []
    summa = []
    new_list = file.read().split("\n")
    for i in new_list:
        i = i.split()
        if int(i[1]) < 20000:
            workers.append(i[0])
        summa.append(i[1])
print(
    f'Оклад меньше 20.000 {workers}, средний оклад {sum(map(int, summa)) / len(summa)}')

# Задание №4
rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('task4.txt', 'r', encoding='utf-8') as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)

with open('file_4_new.txt', 'w', encoding='utf-8') as file_obj_2:
    file_obj_2.writelines(new_file)

# Задание №5
with open('task5.txt', 'r', encoding='utf-8') as numb_file:
    lines = numb_file.read().split()
    x = [int(x) for x in lines]
    for i in x:
        res = sum(x)

print(res)

# Задание №6
with open('task6.txt', 'r', encoding='utf-8') as obj_file:
    lines = obj_file.read().splitlines()
    dic = {}
    for line in lines:
        subject, lecture, practice, lab = line.split()
        dic[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предмету - \n {dic}')
print(dic)


