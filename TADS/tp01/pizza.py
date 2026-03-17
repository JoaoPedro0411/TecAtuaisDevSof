pizzas = ["calabresa", "4 queijos", "frango", "chocolate", "sorvete", "vento", "chuchu", "abacaxi"]

for pizza in pizzas:
    print(f"Eu gosto de pizza sabor {pizza}!")
print(f"Pizza é muito bom!")


print("Os tres primeiros elementos da lista sao: ", end="")

for pizza in pizzas[:3]:
    
    print(f"{pizza}, ", end="")

meio = len(pizzas)//2
print()
print("Os tres elementos que ficam no meio da lista sao: ", end="")
for pizza in pizzas[meio-1:meio+2]:
    print(f"{pizza}, ", end="")

print()

print("Os tres ultimos items da lista sao: ", end="")

for pizza in pizzas[-3:]:
     print(f"{pizza}, ", end="")
    
