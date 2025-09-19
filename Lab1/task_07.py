s = int(input('Введите количество секунд:'))
a = s // 60
b = s - a * 60
result = (a,'Минут', b,'Секунд')
print(result)
