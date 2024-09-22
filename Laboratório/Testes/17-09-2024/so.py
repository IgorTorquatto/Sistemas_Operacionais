import random 

class Processo:
    def __init__(self, id_processo):
        self.id_processo = id_processo
        self.tempo_execucao = random.randint(1,15)
        self.prioridade = random.randint(1,5)
        self.execucao_restante = self.tempo_execucao
    
    def reduzTempo(self, tempo):
        self.execucao_restante -= tempo
        
    def resetTempo(self):
        self.execucao_restante = self.tempo_execucao
    
    def zeraTempo(self):
        self.execucao_restante = 0

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
    tamanho = len(processos)
    for processo in processos:
        tempo_total += processo.tempo_execucao
    tempo_medio = tempo_total/tamanho
    tempo_total = 0
    count = 0
    print(tempo_medio)
    while processos:
        if count == tamanho:
            for processo in processos:
                Processo.resetTempo(processo)
                processos.remove(processo)
        else:
            count = 0          
            for processo in processos:
                if processo.execucao_restante > 0:    
                    print(f"Tempo [{tempo_total}]:  Executando Processo {processo.id_processo} por {processo.tempo_execucao} unidades de tempo.")
                if processo.execucao_restante <= tempo_medio:               
                    tempo_total += processo.execucao_restante
                    Processo.zeraTempo(processo)
                    count += 1
                else:
                    tempo_total += tempo_medio
                    Processo.reduzTempo(processo,tempo_medio)



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
    roundR(processos)
