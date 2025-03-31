import random

from matplotlib import pyplot as plt
from timer import *
from inserctionSort import *
from mergeSort import *
import pandas as pd


def gerar_lista_parcialmente_ordenada(tamanho, percentual_ordenado=0.7):
    parte_ordenada = int(tamanho * percentual_ordenado)
    arr = list(range(parte_ordenada)) + [random.randint(0, 1000000) for _ in range(tamanho - parte_ordenada)]
    return arr

tamanhos = list(range(0, 501, 50))
tempos_insertion = []
tempos_merge = []

for tamanho in tamanhos:
    arr1 = gerar_lista_parcialmente_ordenada(tamanho)
    arr2 = arr1[:]
   
    tempo_insertion = medir_tempo(insertion_sort, arr1)
    tempo_merge = medir_tempo(merge_sort, arr2)

    tempos_insertion.append(tempo_insertion)
    tempos_merge.append(tempo_merge)

    print(f"Tamanho {tamanho}: Insertion = {tempo_insertion:.6f}s, Merge = {tempo_merge:.6f}s")
    
print(arr1)
print(arr2)
df = pd.DataFrame({
    "Tamanho": tamanhos,
    "InsertionSort": tempos_insertion,
    "MergeSort": tempos_merge
})

plt.figure(figsize=(10, 6))
plt.plot(df["Tamanho"], df["InsertionSort"], label="Insertion Sort (Parcialmente Ordenado)", color="red")
plt.plot(df["Tamanho"], df["MergeSort"], label="Merge Sort (Parcialmente Ordenado)", color="blue")
plt.xlabel("Tamanho do Vetor")
plt.ylabel("Tempo de Execução (s)")
plt.title("Desempenho de Insertion Sort e Merge Sort com Entrada Parcialmente Ordenada")
plt.legend()
plt.grid()
plt.show()