# Verifica se a velocidade do veículo está dentro do permitido e calcula a multa.
v = float(input('Digite a velocidade do veículo: '))
if v > 80:
    print('A sua velocidade é de {} km/h e você ultrapassou a velocidade permitida.'.format(v))
    print('A sua multa será no valor de R${:.2f}.'.format((v-80)*7))
print('Dirija com segurança!')
