import time

def medir_tempo(algoritmo, arr):
    inicio = time.perf_counter()
    algoritmo(arr)
    fim = time.perf_counter()
    return fim - inicio