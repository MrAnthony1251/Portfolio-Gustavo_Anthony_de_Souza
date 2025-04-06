import os

LISTA_FILE = "lista_de_fazer.txt"


def carregar_tarefas():
    tarefas = []
    if os.path.exists(LISTA_FILE):
        with open(LISTA_FILE, 'r') as file:
            tarefas = [line.strip() for line in file.readlines()]
    return tarefas


def salvar_tarefas(tarefas):
    with open(LISTA_FILE, 'w') as file:
        for tarefa in tarefas:
            file.write(f"{tarefa}\n")
            
            
            
            
def mostrar_tarefas(tarefas):
    if not tarefas:
        print("Sua lista de fazer está vazia!")
    else:
        print("Sua lista de fazer")
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa}")
            
            
            
def adicionar_tarefas(tarefas):
    tarefa = input("Digite a Entrada: ").strip()
    if tarefa:
        tarefas.append(tarefa)
        salvar_tarefas(tarefas)
        print(f"Adicionar: '{tarefa}'")
    else:
        print("Tarefa não pode estar vazia!")
        
        
        
def deletar_tarefas(tarefas):

    mostrar_tarefas(tarefas)
    if not tarefas:
        return
    
    
    
    
    try:
        tarefa_numero = int(input("Digite numero da tarefa para deletar: "))
        if 1 <= tarefa_numero <= len(tarefas):
            remover_tarefa = tarefas.pop(tarefa_numero - 1)
            salvar_tarefas(tarefas)
            print(f"Deletar: '{remover_tarefa}'")
        else:
            print("Numero de tarefa inválido")
    except ValueError:
        print("Por favor digite o número válido.")
        



def main():
    tarefas = carregar_tarefas()
    
    while True:
        print("\n--- Menu de Lista de Fazer ---")
        print("1. Visualizar tarefas")
        print("2. Adicionar tarefas")
        print("3. Deletar Tarefas")
        print("4. Sair")
        
        escolha = input(("Escolha entre as opções(1-4):"))
        
        if escolha == '1':
            mostrar_tarefas(tarefas)
        elif escolha == '2':
            adicionar_tarefas(tarefas)
        elif escolha == '3':
            deletar_tarefas(tarefas)
        elif escolha == '4':
            print("Até mais!")
            break
        else:
            print("Escolha Inválida. Por favor, tente novamente.")
            
if __name__ == "__main__":
    main()
    
        
     
            
        