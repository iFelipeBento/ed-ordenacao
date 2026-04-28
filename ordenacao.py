# Universidade Federal da Paraíba - Centro de Informática
# Disciplina: Estrutura de Dados e Complexidade de Algoritmos
# Autor: Felipe Bento de Sousa
# Algoritmos: Selection Sort, Insertion Sort, Merge Sort e Quick Sort com análise de custo dinâmico

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

# 3. MERGE SORT
def merge_sort_wrapper(arr):
    print("\n[ Tabela de Execução: Merge Sort ]")
    estado = {'comparacoes': 0, 'movimentacoes': 0, 'passo': 0}

    def merge_sort(lista, inicio, fim):
        if inicio < fim:
            meio = (inicio + fim) // 2
            merge_sort(lista, inicio, meio)
            merge_sort(lista, meio + 1, fim)
            merge(lista, inicio, meio, fim)

    def merge(lista, inicio, meio, fim):
        esquerda = lista[inicio:meio+1]
        direita = lista[meio+1:fim+1]
        i = 0
        j = 0
        k = inicio

        while i < len(esquerda) and j < len(direita):
            estado['comparacoes'] += 1
            if esquerda[i] <= direita[j]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            estado['movimentacoes'] += 1
            k += 1

        # Consome o restante da metade esquerda
        while i < len(esquerda):
            lista[k] = esquerda[i]
            estado['movimentacoes'] += 1
            i += 1
            k += 1

        # Consome o restante da metade direita
        while j < len(direita):
            lista[k] = direita[j]
            estado['movimentacoes'] += 1
            j += 1
            k += 1

        estado['passo'] += 1
        print(f"Passo {estado['passo']} | Array parcial: {lista} | Merge de pos. {inicio} até {fim}")

    merge_sort(arr, 0, len(arr) - 1)
    custo_total = estado['comparacoes'] + estado['movimentacoes']
    print(f">> Custo Final: {estado['comparacoes']} comparações + {estado['movimentacoes']} movimentações = {custo_total} operações")
    return custo_total

# 4. QUICK SORT
def quick_sort_wrapper(arr):
    print("\n[ Tabela de Execução: Quick Sort ]")
    estado = {'comparacoes': 0, 'trocas': 0, 'passo': 0}

    def quick_sort(lista, inicio, fim):
        if inicio < fim:
            pivo_idx = particiona(lista, inicio, fim)
            quick_sort(lista, inicio, pivo_idx - 1)
            quick_sort(lista, pivo_idx + 1, fim)

    def particiona(lista, inicio, fim):
        pivo = lista[fim] # Escolhendo o último elemento como pivô
        i = inicio - 1
        
        for j in range(inicio, fim):
            estado['comparacoes'] += 1
            if lista[j] <= pivo:
                i += 1
                lista[i], lista[j] = lista[j], lista[i]
                if i != j:
                    estado['trocas'] += 1

        lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
        if i + 1 != fim:
            estado['trocas'] += 1

        estado['passo'] += 1
        print(f"Passo {estado['passo']} | Array: {lista} | Pivô ({pivo}) fixado na pos. {i+1}")
        return i + 1

    quick_sort(arr, 0, len(arr) - 1)
    custo_total = estado['comparacoes'] + estado['trocas']
    print(f">> Custo Final: {estado['comparacoes']} comparações + {estado['trocas']} trocas = {custo_total} operações")
    return custo_total


# 5. SORTEIO E TESTE EXECUTÁVEL
if __name__ == "__main__":
    print("="*60)
    print(" Teste de Complexidade: Selection vs Insertion vs Merge vs Quick")
    print("="*60)
    
    # Sorteia 5 números únicos entre 1 e 99
    # (Tamanho pequeno: algoritmos O(N^2) podem surpreender os O(N log N))
    numeros = random.sample(range(1, 100), 5)
    print(f"Array original (Sorteado): {numeros}")
    
    # Criamos cópias exatas para que a comparação seja justa
    arr_selecao = numeros.copy()
    arr_insercao = numeros.copy()
    arr_merge = numeros.copy()
    arr_quick = numeros.copy()
    
    # Executa os algoritmos e guarda o custo (número de operações)
    custo_sel = selection_sort(arr_selecao)
    custo_ins = insertion_sort(arr_insercao)
    custo_mer = merge_sort_wrapper(arr_merge)
    custo_qui = quick_sort_wrapper(arr_quick)
    
    # Veredito de Custo - Criando um Ranking
    resultados = {
        "Selection Sort": custo_sel,
        "Insertion Sort": custo_ins,
        "Merge Sort": custo_mer,
        "Quick Sort": custo_qui
    }
    
    # Ordena os dicionários pelo valor do custo (do menor para o maior)
    ranking = sorted(resultados.items(), key=lambda x: x[1])

    print("\n" + "="*60)
    print(" Dados finais da execução geral - Ranking de Custo")
    print("="*60)
    
    for i, (algo, custo) in enumerate(ranking):
        print(f"{i+1}º Lugar: {algo} com {custo} operações")
        
    vencedor = ranking[0][0]
    
    print("\n[ Análise e Justificativa ]")
    print("Como o array possui apenas 5 elementos (tamanho muito pequeno), o peso do")
    print("gerenciamento recursivo e as movimentações de sub-listas (overhead) penalizam")
    print("o Merge Sort e, por vezes, o Quick Sort.")
    print("\nComportamentos observados:")
    print("- Insertion Sort brilha em listas pequenas ou levemente ordenadas graças ao 'break'.")
    print("- Selection Sort tem custo de comparação alto e fixo, mas economiza em trocas físicas.")
    print("- Merge Sort é extremamente estável O(N log N), mas faz muita movimentação de ")
    print("  arrays auxiliares durante a junção (merge).")
    print("- Quick Sort depende muito do pivô sorteado (neste código, pegamos sempre o último).")
    print("  Se o pivô for ruim, sua eficiência cai, fazendo muitas comparações.")
    
    print(f"\n>> Nesta rodada específica, o vencedor por menor número de operações base foi o {vencedor}!")
    
    print("="*60 + "\n")
