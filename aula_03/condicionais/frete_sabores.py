TAXA = 5 # Forma de utilizar uma "constante".

distancia = int(input("Informe em KM a distância da sua casa: "))
valor_menor_5 = 1
valor_menor_10 = 2

if distancia <= 5:
    frete = TAXA + (distancia * valor_menor_5)
    print(f'💳 O valor do frete é de R${frete}')
elif distancia <= 10:
    frete = TAXA + (distancia * valor_menor_10)
    print(f'💳 O valor do frete é de R${frete}')
else:
    print("⚠️ Infelizmente, não entregamos nessa distância.")