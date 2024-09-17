import os
import time
import signal

def terminar_processo(pid):
    try:
        os.kill(pid, signal.SIGTERM)
        print(f"Enviando sinal SIGTERM para o processo {pid}")
    except OSError as e:
        print(f"Erro ao enviar sinal: {e}")

pid = os.fork()

if pid > 0:
    print("Eu sou o processo pai, meu PID é:", os.getpid())
    print("Esperando o filho terminar...")

    # Permita que o processo filho execute por algum tempo
    time.sleep(5)

    # Envie o sinal SIGTERM para o processo filho
    terminar_processo(pid)

    # Aguarde o término do processo filho
    child_pid, status = os.wait()

    if os.WIFEXITED(status):
        exit_status = os.WEXITSTATUS(status)
        print(f"O processo filho {child_pid} terminou normalmente com status de saída: {exit_status}")
    else:
        print(f"O processo filho {child_pid} não terminou normalmente.")
else:
    print("Eu sou o processo filho, meu PID é:", os.getpid())
    while True:
        # Simula uma tarefa infinita
        time.sleep(1)
        print("Processo filho ainda está rodando...")
