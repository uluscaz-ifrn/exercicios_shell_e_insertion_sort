import time 

def shell_sort(list:list[int]):
    list_size = len(list)
    gap = list_size // 2
    while gap > 0 :
        for i in range(0, list_size-gap):
            aux = list[i]
            if list[i + gap] < aux:
                list[i] = list[i + gap]
                list[i + gap] = aux 
        gap-=1
    return list



def insertion(lista:list[int], indice: int) -> list[int]:
    i = indice # início
    while (i > 0): #condição de parada
        if lista[i-1] > lista[i]:
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

lista = [6.7, 8.5, 5.4, 9.0, 7.8]

# Tempo de execução do shell sort
inicio1 = time.perf_counter()
shell_sort(lista)
fim1  = time.perf_counter()
tempo_shell_sort = inicio1 - fim1

# Tempo de execução do insertion sort
lista_copy = lista.copy()  # Faz uma cópia da lista original para o insertion sort
inicio2 = time.perf_counter()
insertion_sort(lista_copy)
fim2 = time.perf_counter()
tempo_insertion_sort = inicio2 - fim2

print(f"Tempo de execução do shell sort: {tempo_shell_sort} segundos")
print(f"Tempo de execução do insertion sort: {tempo_insertion_sort} segundos")
