import time

COUNT = 50000000


def contar_decrescente(ls, li):
    while ls > li:
        ls -= 1


inicio = time.time()
contar_decrescente(COUNT, 0)
fim = time.time()
print(f'Tempo em segundos: {fim - inicio}')


# Pergunta 1.1 - A função contar_decrescente recebe 2 valores como parâmetro, COUNT e 0 neste caso.
# A função vai decrementando o valor de ls até ls > li. No final é feito o print do tempo de execução.

# Pergunta 1.2 - O programa é CPU-Bound porque o tempo que os cálculos levam a ser efetuados é exclusivamente
# limitado pela velocidade do processador.
