nomes = ['Zezin', 'Huguin', 'Pedrin', 'Jãozin', "Margarida"]

nomes.append('Juquinha')

for nome in nomes: 
    print(f"Sou amigo do {nome}")
    print(f"Olá {nome}, é muito bom ser seu amigo!")
    
print(f"Tenho {len(nomes)} amigos")


for value in range(5):
    print(value)

squares = []
    
for number in range(1,11):
    squares.append(number ** 2)
    
print(squares)
print("---------------------------------------------------")
new_squares = [number ** 2 for number in range(1,11)]

print(new_squares)



numeros = list(range(20,41))
print(numeros)

quad = []

for numero in numeros:
    quad.append(numero ** 2)
   
print(quad)
print(f"A soma dos quadrados de 20 a 40 é: {sum(quad)}")


quadradosNovo = [valor ** 2 for valor in range(20,41) if valor % 2 == 0 ]



matriz = [[i * j for j in range(1,4)] for i in range(1,4)]
for item in matriz:
    print(item)


    
numbers = list(range(1, 1000001))

print(sum(numbers))


multiplos_3 = list(range(3, 31, 3))

for num in multiplos_3: 
    print(num)
    
    
    
lista_cubos = [valor ** 3 for valor in range(1,11)]


novos_amigos = ["Huguinho", "Zezinho", "Luizinho", "Margarida", "Donald", "Patinhas"]


print(novos_amigos[0:3])

print(novos_amigos[2:4])

amigos=novos_amigos[:]

amigos.pop()
print(novos_amigos)
