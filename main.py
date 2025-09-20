def maxmin_select(arr, low, high):
    """
    Algoritmo de seleção simultânea do maior e menor elemento usando divisão e conquista.
    
    Args:
        arr: Lista de números para encontrar o máximo e mínimo
        low: Índice inicial do subvetor
        high: Índice final do subvetor
    
    Returns:
        tuple: (menor_elemento, maior_elemento)
    """
    # Caso base 1: apenas um elemento
    if low == high:
        return arr[low], arr[low]
    
    # Caso base 2: dois elementos
    if high == low + 1:
        if arr[low] <= arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]
    
    # Divisão: encontra o ponto médio
    mid = (low + high) // 2
    
    # Conquista: resolve recursivamente as metades esquerda e direita
    min_left, max_left = maxmin_select(arr, low, mid)
    min_right, max_right = maxmin_select(arr, mid + 1, high)
    
    # Combinação: encontra o mínimo e máximo globais
    global_min = min(min_left, min_right)
    global_max = max(max_left, max_right)
    
    return global_min, global_max


def maxmin_wrapper(arr):
    """
    Função wrapper para facilitar o uso do algoritmo MaxMin Select.
    
    Args:
        arr: Lista de números
    
    Returns:
        tuple: (menor_elemento, maior_elemento) ou None se lista vazia
    """
    if not arr:
        return None
    
    if len(arr) == 1:
        return arr[0], arr[0]
    
    return maxmin_select(arr, 0, len(arr) - 1)


def print_resultado(arr, resultado):
    """
    Imprime o resultado da busca do máximo e mínimo.
    
    Args:
        arr: Lista original
        resultado: Tupla com (mínimo, máximo)
    """
    if resultado is None:
        print("Lista vazia - nenhum resultado")
        return
    
    min_val, max_val = resultado
    print(f"Array: {arr}")
    print(f"Menor elemento: {min_val}")
    print(f"Maior elemento: {max_val}")
    print("-" * 40)


def main():
    """
    Função principal para demonstrar o algoritmo MaxMin Select.
    """
    # Casos de teste
    casos_teste = [
        [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],
        [10, 5, 15, 3, 8, 12],
        [42],
        [1, 2],
        [100, 50, 75, 25, 90, 10],
        [-5, -1, -10, -3, -8],
        [7, 7, 7, 7],
        []
    ]
    
    print("=== Algoritmo MaxMin Select - Divisão e Conquista ===\n")
    
    for i, caso in enumerate(casos_teste, 1):
        print(f"Teste {i}:")
        resultado = maxmin_wrapper(caso)
        print_resultado(caso, resultado)


if __name__ == "__main__":
    main()