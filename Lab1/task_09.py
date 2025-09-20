ip = input('Введите IP для проверки на корректность:\n')
ip = ip.split('.')
ip_parts = [int(part) for part in ip]
if not ip:
    print('Строка пустая!')
else:
    if len(ip) != 4:
        print('Неверный формат IP адреса!')
    else:
        if ip_parts[0] < 0 or ip_parts[0] > 255:
            print('Неверное число в первой части IP:')
        else:
            if ip_parts[1] < 0 or ip_parts[1] > 255:
                print('Неверное число во второй части IP:')
            else:
                if ip_parts[2] < 0 or ip_parts[2] > 255:
                    print('Неверное число в третьей части IP:')
                else:
                    if ip_parts[3] < 0 or ip_parts[3] > 255:
                        print('Неверное число в четвертой части IP:')
                    else:
                        ip_end = '.'.join(str(part) for part in ip_parts)
                        print('Ваш IP', ip_end, 'корректный')

# знаю, что можно было короче, но я хотел, чтобы писало в какой именно части ip ошибка