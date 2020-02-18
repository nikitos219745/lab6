while True:
    try:
        t=int(input('Input time '))
    except ValueError :
        print('INPUT TIME!!')
    a=t%6
    if 1<=a<=3:
        print('Glowing green')
    elif a==4:
        print('Glowing yellow')
    else:
        print('Glowing red')
    n = input("Введи число 1 якщо хочеш продовжити ")
    if n == '1':
        continue
    else:
        break
