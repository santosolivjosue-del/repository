nome = input('nome:')
peso = float(input('seu peso:'))
altura = float(input('sua altura:'))

imc = peso / (altura * altura)

if imc <= 16.9:
    print('resultado:muito abaixo do peso')
elif imc <= 18.4:
    print('resultado:abaixo do peso')
elif imc <= 24.9:
    print('resultado:peso normal')
elif imc <= 29.9:
    print('resultado:acima do peso')
elif imc <= 34.9:
    print('resultado:obesidade grau1')
elif imc <= 40:
    print("resultado:obesidade grau2")
elif imc > 40 :
    print('resultado:obesidade grau3')   
    
print('vai no medico vagabundo')
