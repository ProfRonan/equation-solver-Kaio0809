grau = int(input("Escreva o grau da equação: "))
if 1>grau or grau>2:
    print('Grau inválido')
else:
    if grau == 1:
        print('A equação é do primeiro grau')
        a = int(input('Digite o valor de a: '))
        if a == 0:
            print('Valor de a inválido')
        else:
            b = int(input('Digite o valor de b: '))
            x = -b/a
            print(f'{x:.2f}')
    if grau == 2:
        print('A equação é do segundo grau')
        a = int(input('Digite o valor de a: '))
        if a == 0:
            print('Valor de a inválido')
        else: 
            b = int(input('Digite o valor de b: '))
            c = int(input('Digite o valor de c: '))
            delta = (b**2) - (4*a*c)
            raiz = delta**0.5
            if delta < 0:
                print('A equação não possui raízes reais')
            elif delta == 0:
                print('A equação possui uma raiz real')
                x = (-b + delta**0.5)/2*a
                print(f'x = {x:.2f}')
            elif delta > 0: 
                print('A equação possui duas raízes reais')
                x1 = (-b + raiz)/(2*a)
                x2 = (-b - raiz)/(2*a)
                print(f'x1 = {x1:.2f}')
                print(f'x2 = {x2:.2f}')
