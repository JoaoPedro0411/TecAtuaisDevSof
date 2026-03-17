alien_0 = {'color':'green', 
           'points':5,
           0:"primeiro",
           ('teste', 1): "tupla"
           }

alien_0['alive'] = True



alien_0['points'] = 0
alien_0['alive'] = False


print(alien_0['color'])
print(alien_0['points'])
print(alien_0['alive'])


del alien_0['alive']

print(alien_0)



amigos_linguagens = {
    "Phil" : "JavaScript", 
    "Andrei" : "Python", 
    "Thales" : "C#",
    "Junin" : "Python"
}

print(f" Phil gosta de {amigos_linguagens['Phil']}")


for chave, valor in amigos_linguagens.items():
    print(f"{chave} gosta muito da linguagem {valor}")


print(amigos_linguagens.get('Magalu', "Não tem nenhum amigo com esse"))



print(f" Phil gosta de {amigos_linguagens['Phil']}")


print(f"Meus amigos que responderam a pesquisa sao: ", end ="")

for i in amigos_linguagens.keys(): 
    print(i, end=" ")


print()


print(amigos_linguagens.values())

values = list(amigos_linguagens.values())
values_set = set(amigos_linguagens.values())
print(values)
print(values_set)


numbers_set = {1, 2, 3, 4, 4}

print(numbers_set)

print("As linguagens escolhidas foram: ", end="")
for valor in values_set:
    print(valor, end=" ")