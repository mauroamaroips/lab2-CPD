import multiprocessing as mp
from timeit import default_timer as timer

import numpy as np


def quadrado(nums):
    pnome = mp.current_process().name
    for num in nums:
        res = num * num
        print(f"Processo {pnome}; o quadrado do número {num} é {res}.")


if __name__ == '__main__':
    numero_CPUs = mp.cpu_count()
    processos = []
    limite_superior = 200
    lista = np.array_split(range(limite_superior), numero_CPUs)
    print('Início do multiprocessamento')
    inicio = timer()
    for i in range(numero_CPUs):
        processo = mp.Process(target=quadrado, args=(lista[i],))
        processos.append(processo)
        processo.start()
    for processo in processos:
        processo.join()
    fim = timer()
    print(f"Multiprocessamento completo em {fim-inicio} segundos")
    print('Início do multiprocessamento com pool')
    pool = mp.Pool(processes=numero_CPUs)
    inicio = timer()
    resultado = pool.map(quadrado, lista)
    fim = timer()
    print(f"Multiprocessamento completo em {fim - inicio} segundos")


# Pergunta 5.1 -
# lista = np.array_split(range(limite_superior), numero_CPUs): é criado um array de arrays tendo em conta dois argumentos
# de forma a equilibrar o número de elementos dos sub-arrays
# processo = mp.Process(target=quadrado, args=(lista[i],)): recebe 2 argumentos (quadrado e o index de um dos subarrays)
# de forma a calcular o quadrado dos números presentes dentro destes
# processos.append(processo): adiciona a um array de processos cada processo
# processo.start(): inicialização de um processos
# processo.join(): espera que um processo termine de forma a executar

# Pergunta 5.2 -
# Sem pool: 12 processos
# Com pool: 1 processo

# Pergunta 5.3 - A pool apresenta tempos de execução melhores pois a pool cria todos os processos antes de os usar e coloca-os
# numa qeue, se um processo receber trabalho e processar todos os valores, os outros processos nunca serão executados e são mortos.
# Na execução de processos, um array é dividido num array de arrays e os valores são processados paralelamente, fazendo
# com que os processos tenham que aceder ao processador de forma a receber trabalho.



