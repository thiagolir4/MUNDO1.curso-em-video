v = float(input('Seu carro passou pelo radar a  km/h'))
multa = float((v-70) * 7)
if v > 70:
    print('você foi multado, sua multa é de {:.2f}'.format(multa))
else: 
    print('você está dentro da velocidade permitida')
