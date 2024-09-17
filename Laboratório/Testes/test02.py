import os
import time

pid = os.fork()

if pid > 0:
    print("Eu sou o processo pai, meu PID é", os.getpid())
    print("Esperando o processo filho terminar...")
    os.wait() #Aguarda o término do processo filho
    print("O processo filho terminou")
else:
    print("Eu sou o processo filho, meu PID é",os.getpid())
    time.sleep(2)
    print("Processo filho terminado.")

