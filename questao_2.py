def insertion(lista:list[int], indice: int) -> list[int]:
    i = indice # início
    while (i > 0): #condição de parada
        if lista[i-1][1] > lista[i][1]:
            aux = lista[i-1]
            lista[i-1] = lista[i]
            lista[i] = aux
        else:
            break
        i-= 1 #passo
    return lista

def insertion_sort(lista:list[int]) -> list[int]:
    i = 1 #início
    while (i < len(lista)): #condição de parada
        lista = insertion(lista,i)
        i+=1 # passo
        
    return lista

pessoas = [
    ("Ana", 25),
    ("Bruno", 30),
    ("Carlos", 22),
    ("Diana", 28),
    ("Eduardo", 35)
]

print(insertion_sort(pessoas))