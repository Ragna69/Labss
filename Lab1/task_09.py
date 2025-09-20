ip = input('Введите IP для проверки на корректность:\n')
ipp = ip.split('.')
if not ip:
    print('Строка пустая!')
else:
    if len(ipp) != 4:
        print('Неверный формат IP адреса!')
    else:
        if not ipp[0].isdigit() or 0 > int(ipp[0]) > 255 or not\
             ipp[1].isdigit() or 0 > int(ipp[1]) > 255 or not\
             ipp[2].isdigit() or 0 > int(ipp[2]) > 255 or not \
             ipp[3].isdigit() or 0 > int(ipp[3]) > 255:
            print('Ваш IP', ip, 'некорректный')
        else:
            print('Ваш IP', ip, 'корректный')