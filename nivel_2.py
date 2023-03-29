# threads Múltiplos
import time
from threading import Thread

COUNT = 50000000


def contar_decrescente(ls, li):
    while ls > li:
        ls -= 1


inicio = time.time()
thread_1 = Thread(target=contar_decrescente, args=(COUNT, COUNT // 2,))
thread_2 = Thread(target=contar_decrescente, args=(COUNT // 2, 0,))
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()
fim = time.time()
print(f'Tempo em segundos: {fim - inicio}')

# Pergunta 2.1 - Este algoritmo faz uso de diferentes threads de forma a processar mais rapidamente os cálculos
# presentes na função contar_decrescente.

# Pergunta 2.2 - O tempo de execução do nível 2 para o nível 1 é ligeiramente superior visto que duas threads
# não correm em paralelo (esperam sim uma pela outra). Esta troca entre threads faz com que seja perdido tempo.