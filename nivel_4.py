import multiprocessing
import random
from timeit import default_timer as timer


def criar_e_ordenar(n):
    rand = random.Random(50)
    x = [rand.randint(0, 100) for _ in range(n)]
    x.sort()
    return x


if __name__ == "__main__":
    numero_CPUs = multiprocessing.cpu_count()
    print(f'Número de CPUs: {numero_CPUs}')
    vetores_a_gerar = [2, 4, 6, 15]
    dimensoes_dos_vetores = [10 ** 2, 10 ** 3, 10 ** 4, 10 ** 6]
    for numero_de_elementos in dimensoes_dos_vetores:
        print(f'Número elementos do vetor: {numero_de_elementos}')
        for qtd_vetores_a_gerar in vetores_a_gerar:
            print(f'\tQuantidade de vetores a gerar e ordenar: {qtd_vetores_a_gerar}')
            dimensoes = []
            for i in range(qtd_vetores_a_gerar):
                dimensoes.append(numero_de_elementos)
            # dimensoes1 = [d for i in range(qtd_vetores_a_gerar)]
            # print(dimensoes ,dimensoes1)
            # Aplicar a função sequencialmente
            resultado = []
            inicio = timer()
            for d in dimensoes:
                resultado.append(criar_e_ordenar(d))
            # resultado = [createandsort(d) for d in dimensoes]
            fim = timer()
            print("\t\tTempo para ordenação sequencial: ", fim - inicio)
            # print(resultado)
            # print([createandsort(d) for d in dimensoes])

            # Utilizando multiprocessamento
            pool = multiprocessing.Pool(processes=numero_CPUs)  # Usa o número de cores físicos da sua máquina
            inicio = timer()
            resultado = pool.map(criar_e_ordenar, dimensoes)
            fim = timer()
            print("\t\tTempo para ordenação paralela: ", fim - inicio)

# Pergunta 4.1 - pool = multiprocessing.Pool(processes=numero_CPUs): cria worker processes tendo
# em conta os cores físicos e virtuais da máquina (12 no caso da máquina em que estou a trabalhar neste momento)
# pool.map(createandsort, dimensoes): é usado para executar determinadas funções para todos os processos presentes na pool

# Pergunta 4.2 - Por vezes, criar processos não gera ganhos em termos de tempo de execução.
# Sempre que são criados processos são replicados ambientes python, logo o tempo perdido na replicação
# não compensa o tempo de execução de vetores de pequena dimensão, mas é possível observar grandes ganhos de tempo
# quando temos vetores de dimensão considerável.

