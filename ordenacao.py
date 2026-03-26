# Universidade Federal da Paraíba - Centro de Informática
# Disciplina: Estrutura de Dados e Complexidade de Algoritmos
# Autor: Felipe Bento de Sousa
# Algoritmos: Selection Sort e Insertion Sort com análise de custo dinâmico

import random

# 1. SELECTION SORT
def selection_sort(arr):
    print("\n[ Tabela de Execução: Selection Sort ]")
    n = len(arr)
    comparacoes = 0
    trocas = 0

    for i in range(n - 1):
        min_idx = i
        # Procura o menor elemento no restante da lista
        for j in range(i + 1, n):
            comparacoes += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Se achou um número menor, faz a troca
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            trocas += 1
            
        print(f"Passo {i+1} | Array: {arr} | Menor encontrado e posicionado: {arr[i]}")

    custo_total = comparacoes + trocas
    print(f">> Custo Final: {comparacoes} comparações + {trocas} trocas = {custo_total} operações")
    return custo_total

# 2. INSERTION SORT
def insertion_sort(arr):
    print("\n[ Tabela de Execução: Insertion Sort ]")
    n = len(arr)
    comparacoes = 0
    deslocamentos = 0

    for i in range(1, n):
        key = arr[i] # A 'carta' que vamos inserir
        j = i - 1
        
        # Empurra os maiores para a direita
        while j >= 0:
            comparacoes += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                deslocamentos += 1
                j -= 1
            else:
                break # Achou a posição certa
                
        arr[j + 1] = key
        print(f"Passo {i} | Array: {arr} | Chave ({key}) inserida na posição correta")

    custo_total = comparacoes + deslocamentos
    print(f">> Custo Final: {comparacoes} comparações + {deslocamentos} deslocamentos = {custo_total} operações")
    return custo_total

# 3. SORTEIO E TESTE EXECUTÁVEL
if __name__ == "__main__":
    print("="*50)
    print(" Teste de execução em comparação entre Insertion Sort & Selection Sort")
    print("="*50)
    
    # Sorteia 5 números únicos entre 1 e 99
    numeros = random.sample(range(1, 100), 5)
    print(f"Array original (Sorteado): {numeros}")
    
    # Criamos cópias exatas para que a comparação seja justa
    arr_selecao = numeros.copy()
    arr_insercao = numeros.copy()
    
    # Executa os algoritmos e guarda o custo (número de operações)
    custo_sel = selection_sort(arr_selecao)
    custo_ins = insertion_sort(arr_insercao)
    
    # Veredito de Custo
    print("\n" + "="*50)
    print(" Dados finais da execução geral")
    print("="*50)
    if custo_sel < custo_ins:
        print(f"O Selection Sort foi MAIS BENÉFICO neste caso, sendo ({custo_sel} vs {custo_ins} operações).")
        print("\n[ Justificativa? ]")
        print("Os números sorteados vieram muito desordenados (provavelmente de trás pra frente).")
        print("O Insertion Sort sofre muito com isso, pois é forçado a empurrar (deslocar) quase todos")
        print("os números a cada passo. O Selection Sort, apesar de fazer muitas comparações fixas,")
        print("fez pouquíssimas trocas físicas, acabando por ser mais eficiente nesta rodada.")
        
    elif custo_ins < custo_sel:
        print(f"O Insertion Sort foi MAIS BENÉFICO neste caso, sendo ({custo_ins} vs {custo_sel} operações).")
        print("\n[ Justificativa? ]")
        print("Os números sorteados já vieram um pouco pré-organizados. O Insertion Sort tira vantagem")
        print("disso: assim que ele acha o lugar da carta, ele para de comparar (graças ao comando 'break').")
        print("Já o Selection Sort é 'teimoso' e obrigatoriamente faz todas as comparações possíveis,")
        print("mesmo que o array já esteja ordenado, o que o tornou mais custoso.")
        
    else:
        print(f"Empate! Ambos tiveram um custo exato de {custo_sel} operações nesta configuração.")
        print("\n[ Justificativa? ]")
        print("Um caso raro de sorteio! O nível de bagunça do array gerou um balanço exato")
        print("entre as comparações fixas do Selection Sort e os deslocamentos do Insertion Sort.")
        
    print("="*50 + "\n")
