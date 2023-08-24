preço = float(input('Digite o valor do seu produto R$'))
desconto = preço *5 / 100
print('O seu produto custa R${:.2f}, e tem R${:.2f} de desconto, o valor final dele é de R${:.2f}'.format(preço, desconto, preço-desconto))