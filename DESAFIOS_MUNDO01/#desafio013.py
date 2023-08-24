salario = float(input('Qual o salário do seu funcionário R$'))
aumento = float(salario * 15 / 100)
print('Seu aumento de salário foi de 15%, o valor do reajuste final é de {:.2f} e seu salário vai passar a ser de {:.2f}'.format(aumento, salario + aumento))