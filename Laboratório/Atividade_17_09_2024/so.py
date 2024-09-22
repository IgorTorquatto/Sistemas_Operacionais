import random

class Processo:
    def __init__(self, id_processo):
        self.id_processo = id_processo
        self.tempo_execucao = random.randint(1, 15)
        self.prioridade = random.randint(1, 5)
        self.execucao_restante = self.tempo_execucao
    
    def reduzTempo(self, tempo):
        self.execucao_restante -= tempo
        
    def resetTempo(self):
        self.execucao_restante = self.tempo_execucao
    
    def zeraTempo(self):
        self.execucao_restante = 0

def fifo_escalonamento(processos):
    #Executa os processos na ordem de chegada.
    tempo_total = 0
    for processo in processos:
        print(f"Tempo [{tempo_total}]:  Executando Processo {processo.id_processo} por {processo.tempo_execucao} unidades de tempo.")
        tempo_total += processo.tempo_execucao

def sjf(processos):
    #Executa primeiro o processo com o menor tempo de execução.
    tempo_total = 0
    processos.sort(key=lambda obj: obj.tempo_execucao)
    for processo in processos:
        print(f"Tempo [{tempo_total}]:  Executando Processo {processo.id_processo} por {processo.tempo_execucao} unidades de tempo.")
        tempo_total += processo.tempo_execucao

def roundR(processos):
    #Divide o tempo igualmente entre os processos, alternando entre eles.
    tempo_total = 0
    tamanho = len(processos)
    for processo in processos:
        tempo_total += processo.tempo_execucao
    tempo_medio = tempo_total / tamanho
    tempo_total = 0
    count = 0
    while processos:
        if count == tamanho:
            for processo in processos:
                processo.resetTempo()
                processos.remove(processo)
        else:
            count = 0          
            for processo in processos:
                if processo.execucao_restante > 0:    
                    print(f"Tempo [{tempo_total}]:  Executando Processo {processo.id_processo} por {processo.tempo_execucao} unidades de tempo.")
                if processo.execucao_restante <= tempo_medio:               
                    tempo_total += processo.execucao_restante
                    processo.zeraTempo()
                    count += 1
                else:
                    tempo_total += tempo_medio
                    processo.reduzTempo(tempo_medio)

def prioridade(processos):
    #Executa os processos com base na prioridade definida.
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
    
    print("Escolha o algoritmo de escalonamento:")
    print("1. FIFO")
    print("2. Shortest Job First (SJF)")
    print("3. Round Robin")
    print("4. Prioridade")
    
    escolha = input("Digite o número da sua escolha: ")
    
    if escolha == "1":
        print("\nExecutando algoritmo FIFO...\n")
        fifo_escalonamento(processos)
    elif escolha == "2":
        print("\nExecutando algoritmo Shortest Job Firist...\n")
        sjf(processos)
    elif escolha == "3":
        print("\nExecutando algoritmo Round Robin...\n")
        roundR(processos)
    elif escolha == "4":
        print("\nExecutando algoritmo Prioridade..\n")
        prioridade(processos)
    else:
        print("\nEscolha inválida.\n")
