from timer import *
from inserctionSort import *
from mergeSort import *
import random
import pandas as pd
import matplotlib.pyplot as plt

tamanhos = list(range(0, 20001, 50))
tempos_insertion = []
tempos_merge = []

for tamanho in tamanhos:
    arr1 = [random.randint(0, 5000) for _ in range(tamanho)]
    arr2 = arr1[:]  

    tempo_insertion = medir_tempo(insertion_sort, arr1)
    tempo_merge = medir_tempo(merge_sort, arr2)

    tempos_insertion.append(tempo_insertion)
    tempos_merge.append(tempo_merge)

    print(f"Tamanho {tamanho}: Insertion = {tempo_insertion:.6f}s, Merge = {tempo_merge:.6f}s")

print(f"Vetor do Inscerction Sort ordenado: \n{arr1}")
print(f"Vetor do Merge Sort ordenado: \n{arr2}")


df = pd.DataFrame({"Tamanho": tamanhos, "InsertionSort": tempos_insertion, "MergeSort": tempos_merge})
df.to_csv("resultados.csv", index=False)

print("Medição concluída! Os resultados foram salvos em 'resultados.csv'.")


df = pd.read_csv("resultados.csv")

plt.figure(figsize=(10, 6))
plt.plot(df["Tamanho"], df["InsertionSort"], label="Insertion Sort", color="red")
plt.plot(df["Tamanho"], df["MergeSort"], label="Merge Sort", color="blue")

plt.xlabel("N° de elementos")
plt.ylabel("Tempo (s)")
plt.title("Tempo de execução com 20000 elementos")
plt.legend()
plt.grid()
plt.show()
