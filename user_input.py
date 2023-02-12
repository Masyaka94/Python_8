chislo_1 = 0
chislo_2 = 0
oper = ''

def inp(chislo_1, chislo_2):
    if 'j' in chislo_1:
        chislo_1 = complex(chislo_1)
    else:
        chislo_1 = float(chislo_1)
    if 'j' in chislo_2:
        chislo_2 = complex(chislo_2)
    else:
        chislo_2 = float(chislo_2)
    return (chislo_1, chislo_2)


def inp2():
    global chislo_1
    global chislo_2
    global oper
    chislo_1 = input('Введите первое число: ')
    chislo_2 = input('Введите второе число: ')
    if 'i' in chislo_1:
        chislo_1 = complex(chislo_1)
    else:
        chislo_1 = float(chislo_1)
    if 'i' in chislo_2:
        chislo_2 = complex(chislo_2)
    else:
        chislo_2 = float(chislo_2)
    oper = input('Введите оператор (*, /, -, +,**): ')
    return (chislo_1, chislo_2, oper)