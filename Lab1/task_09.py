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
            a = ip_parts[0]
            if ip_parts[1] < 0 or ip_parts[1] > 255:
                print('Неверное число во второй части IP:')
            else:
                b = ip_parts[1]
                if ip_parts[2] < 0 or ip_parts[2] > 255:
                    print('Неверное число в третьей части IP:')
                else:
                    c = ip_parts[2]
                    if ip_parts[3] < 0 or ip_parts[3] > 255:
                        print('Неверное число в четвертой части IP:')
                    else:
                        d = ip_parts[3]
                        ip_end = '.'.join(str(part) for part in ip_parts)
                        print('Ваш IP', ip_end, 'корректный')