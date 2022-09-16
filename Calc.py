resultado = 0.0
numero1 = 0.0
numero2 = 0.0


def addi(numero1, numero2):
    return float(numero1+numero2)


def subt(numero1, numero2):
    return float(numero1-numero2)


def div(numero1, numero2):
    return float(numero1/numero2)


def multi(numero1, numero2):
    return float(numero1*numero2)


numero1 = float(input('1:'))
numero2 = float(input('2:'))
oper = str(input('oper:'))

if oper == 'addi':
    print(addi(numero1, numero2))
elif oper == 'subt':
    print(addi(numero1, numero2))
elif oper == 'div':
    print(addi(numero1, numero2))
elif oper == 'multi':
    print(addi(numero1, numero2))
else:
    print('no')
