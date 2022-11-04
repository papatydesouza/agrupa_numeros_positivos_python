print ("****** Olá! Seja bem vindo ao jogo de contagem de números positivos ******")

numero = 1
g1 = 0
g2 = 0
g3 = 0
g4 = 0

while (numero > 0):
    numero = int(input("Digite um número de 1 a 100 ou um número negativo para sair! "))
    if (numero > 0 and numero <= 25):
        g1 = g1 + 1
    elif (numero > 25 and numero <= 50):
        g2 = g2 + 1
    elif (numero > 50 and numero <= 75):
        g3 = g3 + 1
    elif (numero > 75 and numero <= 100):
        g4 = g4 + 1

print("A quantidade de números ficou:\n{} de 0 a 25\n{} de 26 a 50\n{} de 51 a 75\n{} de 76 a 100" .format(g1,g2,g3,g4))