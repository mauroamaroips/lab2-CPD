import time
from multiprocessing import Pool


def contar_decrescente(ls, li):
    while ls > li:
        ls -= 1


if __name__ == '__main__':
    COUNT = 50000000
    pool = Pool(2)
    start = time.time()
    pool.apply_async(contar_decrescente, [COUNT//2, 0])
    pool.apply_async(contar_decrescente, [COUNT, COUNT // 2])
    pool.close()
    pool.join()
    end = time.time()
    print('Tempo em segundos: ', end - start)


# Pergunta 3.1 - Neste algoritmo é criada uma pool de 2 processos que farão o decrement de COUNT de forma assíncrona.
# No final é esperado que todos os processos acabem para serem executados os métodos close() e join().

# Pergunta 3.2 - É possível observar quem em relação ao nível 2, o tempo de execução é praticamente cortado para metade
# visto que aqui os processos correm paralelamente de forma assíncrona.

