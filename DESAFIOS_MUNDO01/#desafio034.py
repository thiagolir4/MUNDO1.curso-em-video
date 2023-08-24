sal = float(input('Digite aqui seu salário para que eu consiga calcular seu aumento R$ '))
sal1 = (sal * 10 / 100) + sal
sal2 = (sal * 15 / 100) + sal
if sal > 1250.00:
    print(sal2)
else:
    print(sal1)