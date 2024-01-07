
total_numeros = 0
total_pares = 0
sum_pares = 0
sum_impares = 0
count_menores_10 = 0
count_entre_20_y_50 = 0
count_mayores_100 = 0


while True:
    num = int(input("Ingrese un número (ingrese un número negativo para finalizar): "))

    if num < 0:
        break  

    
    total_numeros += 1

   
    if num % 2 == 0:
        total_pares += 1
        sum_pares += num
    else:
        sum_impares += num


    if num < 10:
        count_menores_10 += 1
    elif 20 <= num <= 50:
        count_entre_20_y_50 += 1
    elif num > 100:
        count_mayores_100 += 1


promedio_pares = sum_pares / total_pares if total_pares > 0 else 0
promedio_impares = sum_impares / (total_numeros - total_pares) if (total_numeros - total_pares) > 0 else 0


print("\nInforme:")
print(f"a. Total de números ingresados: {total_numeros}")
print(f"b. Total de números pares ingresados: {total_pares}")
print(f"c. Promedio de los números pares: {promedio_pares:.2f}")
print(f"d. Promedio de los números impares: {promedio_impares:.2f}")
print(f"e. Cuantos números son menores que 10: {count_menores_10}")
print(f"f. Cuantos números están entre 20 y 50: {count_entre_20_y_50}")
print(f"g. Cuantos números son mayores que 100: {count_mayores_100}")

