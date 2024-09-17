import os

pid = os.fork()

if pid > 0:
    print("Eu sou o processo pai, meu PID é", os.getpid())
    print("O PID do meu filho é", pid)
else:
    print("Eu sou o processo filho, meu PID é",os.getpid())

#getppid retorna o ID do processo pai
#getpid retorna o ID Do processo atual