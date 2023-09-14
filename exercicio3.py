import threading
"""Instanciada a classe Crescente e atrelada a thread: 
   Iniciado o método e utilizado o super() para herança entre as
   duas classes do código"""
class Crescente(threading.Thread):
    def __init__(self, total):
        super().__init__()
        self.total = total
    def run(self):
        for i in range(1, self.total + 1):
            print(i)
class Decrescente(threading.Thread):
    def __init__(self, total):
        super().__init__()
        self.total = total
    def run(self):
        for i in range(self.total, 0, - 1):
            print(i)

if __name__ == "__main__":
    thread_crescente = Crescente(500)
    thread_decrescente = Decrescente(500)

    thread_crescente.start()
    thread_decrescente.start()

    thread_decrescente.join()
    thread_decrescente.join()