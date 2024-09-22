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
    # Escalonamento por ordem de chegada (FIFO)
    tempo_total = 0

    for processo in processos:
        print(f"Tempo [{tempo_total}]:  Executando Processo {processo.id_processo} por {processo.tempo_execucao} unidades de tempo.")
        tempo_total += processo.tempo_execucao

def sjf(processos):
    # Escalonamento por menor tempo de execução (SJF)
    tempo_total = 0
    processos.sort(key=lambda obj: obj.tempo_execucao)

    for processo in processos:
        print(f"Tempo [{tempo_total}]:  Executando Processo {processo.id_processo} por {processo.tempo_execucao} unidades de tempo.")
        tempo_total += processo.tempo_execucao

def roundR(processos):
    # Escalonamento por Round Robin
    tempo_total = 0
    tamanho = len(processos)
    tempo_medio = sum(p.tempo_execucao for p in processos) / tamanho
    count = 0

    while processos:
        if count == tamanho:
            for processo in processos:
                processo.resetTempo()
            count = 0
        else:
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
    # Escalonamento por prioridade
    tempo_total = 0
    processos.sort(key=lambda obj: obj.prioridade)

    for processo in processos:
        print(f"Tempo [{tempo_total}]:  Executando Processo {processo.id_processo} de prioridade {processo.prioridade} por {processo.tempo_execucao} unidades de tempo.")
        tempo_total += processo.tempo_execucao

def mostrar_menu():
    print("\nEscolha um algoritmo de escalonamento:")
    print("1 - FIFO (First In First Out)")
    print("2 - SJF (Shortest Job First)")
    print("3 - Round Robin")
    print("4 - Prioridade")
    print("5 - Sair")
    return input("Digite o número da sua escolha: ")

if __name__ == "__main__":
    while True:
        try:
            # Pergunta ao usuário quantos processos ele quer criar
            num_processos = int(input("\nDigite o número de processos que deseja criar: "))
            if num_processos <= 0:
                print("Número inválido. Por favor, digite um número positivo.")
                continue
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
            continue
        
        # Criando processos a cada execução para garantir novos tempos e prioridades
        processos = [Processo(i) for i in range(1, num_processos + 1)]
        
        escolha = mostrar_menu()

        if escolha == '1':
            print("\nExecutando FIFO...\n")
            fifo_escalonamento(processos)
        elif escolha == '2':
            print("\nExecutando SJF...\n")
            sjf(processos)
        elif escolha == '3':
            print("\nExecutando Round Robin...\n")
            roundR(processos)
        elif escolha == '4':
            print("\nExecutando Prioridade...\n")
            prioridade(processos)
        elif escolha == '5':
            print("Saindo do programa...")
            break
        else:
            print("Escolha inválida. Tente novamente.")
        
        input("\nPressione Enter para voltar ao menu...")  # Pausa antes de voltar ao menu
