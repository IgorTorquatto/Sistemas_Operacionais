import random 

class Processo:
    def __init__(self, id_processo):
        self.id_processo = id_processo
        self.tempo_execucao = random.randint(1,15)
        self.prioridade = random.randint(1,5)

def fifo_escalonamento(processos):
    #Adicionar comentário explicativo

    tempo_total = 0

    for processo in processos:
        print(f"Tempo [{tempo_total}]:  Executando Processo {processo.id_processo} por {processo.tempo_execucao} unidades de tempo.")
        tempo_total += processo.tempo_execucao

def sjf(processos):
    #Adicionar comentário explicativo

    tempo_total = 0
    
    processos.sort(key=lambda obj: obj.tempo_execucao)

    for processo in processos:
        print(f"Tempo [{tempo_total}]:  Executando Processo {processo.id_processo} por {processo.tempo_execucao} unidades de tempo.")
        tempo_total += processo.tempo_execucao

def roundR(processos):
    tempo_total = 0


def prioridade(processos):
    #Adicionar comentário explicativo
    tempo_total = 0

    processos.sort(key=lambda obj: obj.prioridade)

    for processo in processos:
        print(f"Tempo [{tempo_total}]:  Executando Processo {processo.id_processo} de prioridade {processo.prioridade} por {processo.tempo_execucao} unidades de tempo.")
        tempo_total += processo.tempo_execucao


if __name__ == "__main__":
    processos = [
        Processo(1),
        Processo(2),
        Processo(3),
        Processo(4)
    ]
    
    #fifo_escalonamento(processos)
    #sjf(processos)
    #prioridade(processos)

