# execicio de lista

# Criando listas para os números
numeros_1_a_15 = list(range(1, 16))  
numeros_1_a_9 = list(range(1, 10))    
numeros_8_a_13 = list(range(8, 14))    

numeros_pares = []
for num in numeros_1_a_15:
    if num % 2 == 0: 
        numeros_pares.append(num)

numeros_impares = []
for num in numeros_1_a_15:
    if num % 2 != 0:  
        numeros_impares.append(num)

multiplos_2 = []
for num in numeros_1_a_15:
    if num % 2 == 0:
        multiplos_2.append(num)

multiplos_3 = []
for num in numeros_1_a_15:
    if num % 3 == 0:
        multiplos_3.append(num)

multiplos_4 = []
for num in numeros_1_a_15:
    if num % 4 == 0:
        multiplos_4.append(num)

soma_10_a_15 = sum(range(10, 16))  
soma_3_a_9 = sum(range(3, 10))     

razao = soma_10_a_15 / soma_3_a_9    

print("Números de 1 a 15:", numeros_1_a_15)
print("Números de 1 a 9:", numeros_1_a_9)
print("Números de 8 a 13:", numeros_8_a_13)
print("Números pares:", numeros_pares)
print("Números ímpares:", numeros_impares)
print("Múltiplos de 2:", multiplos_2)
print("Múltiplos de 3:", multiplos_3)
print("Múltiplos de 4:", multiplos_4)
print("Razão entre a soma de 10 a 15 e 3 a 9:", razao)
