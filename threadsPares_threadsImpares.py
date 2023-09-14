import threading
import random
import time

"""
Realizado import random e time para definir o tempo que seria executado a thread

 """

def thread_pares(total):
    for i in range (2, total + 1, 2):
        sleep_time = random.uniform(0,1)
        print("Thread pares:", i, "Sleep:", sleep_time)
        time.sleep(sleep_time)
        

def thread_impares(total):
    for i in range(1, total +1, 2):
        sleep_time = random.uniform(0,3)
        print("Thread impares:", i, "Sleep:", sleep_time)
        time.sleep(sleep_time)

if __name__ == "__main__":
    thread_pares = threading.Thread(target=thread_pares, args=(100,))
    thread_impares= threading.Thread(target=thread_impares, args=(100,))

""" Início da execução das Threads"""

thread_pares.start()
thread_impares.start()


thread_pares.join()
thread_impares.join()