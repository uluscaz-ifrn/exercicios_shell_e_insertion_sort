# Inserção Ordenada
def insertion(list: list[float], index: int) -> list[float]:
    # NOTE: Modifiquei o for para ele percorrer do index até 0
    for item in range(index, 0, -1):
        if list[item] > list[item-1]: # Verifica se o item atual é menor que o item que está a sua frente
            aux = list[item] # Variável auxiliar que armazena o item atual
            list[item] = list[item-1] # O item atual é trocado pelo item a sua frente
            list[item-1] = aux # O item atual, que está armazenado na variável auxiliar, percorre uma posição para frente

    # Retorna a lista ordenada
    return list

# Insertion Sort
def insertion_sort(list: list[float]) -> list[float]:
    index = 1 # Variável responsável por armazenar a quantidade de passos do laço
    while (index < len(list)): # Condição de parada
        list = insertion(list, index) # A lista irá receber uma nova lista até que ela esteja totalmente ordenada
        index += 1 # Acrescenta mais 1 a cada passo que o laço fizer

    # Retorna a lista ordenada, após a condição do laço não ser mais verdadeira
    return list

# Lista que irá armazenar as notas finais dos alunos
notas_finais = []

while True:
    # Menu de opções
    opcao = int(input('[1] Adicionar nota\n[0] Finalizar\n-> '))

    # Verifica se o usuário informou o número 0, para finalizar o laço
    if opcao == 0:
        # Verifica se o tamanho da lista é maior que 0
        if len(notas_finais) > 0:
            # Exibe a lista com a sequência informada pelo usuário
            print(f'Entrada: {notas_finais}')
            # Exibe a lista ordenada utilizando o insertion sort
            print(f'Saída: {insertion_sort(notas_finais)}')
        else:
            print('Você não informou nenhum valor.')

        break
    # Verifica se o usuário informou o número 1, para adicionar uma nova nota
    elif opcao == 1:
        # Solicita que o usuário informe a nota
        nota = float(input('Adicione a nota: '))
        # Adiciona a nota na lista de notas finais
        notas_finais.append(nota)

    # Mensagem que será exibida, caso o usuário informe uma opção inválida do menu
    else:
        print('Opção inválida')