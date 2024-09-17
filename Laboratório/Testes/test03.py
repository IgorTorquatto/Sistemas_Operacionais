import os
import time

pid = os.fork()

if pid > 0:
    print("Eu sou o processo pai, meu PID é", os.getpid())
    print("Esperando o processo filho terminar...")
    child_pid, status = os.wait()

    if os.WIFEXITED(status):
        exit_status = os.WEXITSTATUS(status)
        print(f"O processo filho {child_pid} terminou normalmente com status de saída: {exit_status}")
    else:
        print(f"O processo filho {child_pid} não terminou normalmente")
else:
    print("Eu sou o processo filho, meu PID é",os.getpid())
    time.sleep(2)
