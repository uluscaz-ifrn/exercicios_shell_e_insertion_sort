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

lista = [6.7, 8.5, 5.4, 9.0, 7.8]
print(shell_sort(lista))
                

