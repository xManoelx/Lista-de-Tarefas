# Funcao para adicionar uma nova tarefa
def addTask(tarefas, nome_tarefa): 
    
    tarefa = {"name": nome_tarefa, "complete": False}
    tarefas.append(tarefa)
    print(f"A tarefa '{nome_tarefa}' foi adicionada com sucesso!")
    return

# Funcao para visualizar todas as tarefas 
def viewTask(tarefas): 
    
    print("\nLista de tarefas:")
    
    for indice, tarefa in enumerate(tarefas, start=1):
        if tarefa["complete"]: 
            status = "✔"
        else:
            status = " "    

        nome_tarefa = tarefa["name"]
        print(f"{indice}. [{status}] {nome_tarefa}")
    return

# Funcao para atualizar o nome de uma tarefa especifica
def attTaskName(tarefas, indiceTarefa, novoNomeTarefa):
    
    indiceTarefaAjustado = int(indiceTarefa) - 1
    
    if indiceTarefaAjustado >= 0 and indiceTarefaAjustado < len(tarefas):
        tarefas[indiceTarefaAjustado]["name"] = novoNomeTarefa
        print(f"Tarefa {indiceTarefa} atualizada para {novoNomeTarefa}")
    else:
        print("Indice de tarefa inválido.")
    return

# Funcao para marcar uma tarefa especifica como completa
def completeTask(tarefas, indiceTarefa):
    
    indiceTarefaAjustado = int(indiceTarefa) - 1

    tarefas[indiceTarefaAjustado]["complete"] = True
    print(f"Tarefa {indiceTarefa} marcada como completada")
    return

# Funcao para deletar uma tarefa especifica
def deleteTask(tarefas):
    
    for tarefa in tarefas:
        if tarefa["complete"]:
            tarefas.remove(tarefa)
    print ("Tarefas completadas foram deletadas!")
    return

tarefas = []

while True:
    print("\nMenu do Gerenciador de Lista de Tarefas")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Remover tarefa")
    print("6. Sair")

    choose = input("\nDigite a sua escolha: ")

    # Adicionar tarefa
    if choose == "1": 
        nome_tarefa = input("Digite o nome da tarefa: ")
        addTask(tarefas, nome_tarefa)

    # Ver tarefas
    elif choose == "2":    
        viewTask(tarefas)

    # Atualizar tarefa
    elif choose == "3": 
        viewTask(tarefas)
        indiceTarefa = input("Digite o número da tarefa que deseja atualizar: ")
        novoNome = input("Digite o novo nome para a tarefa: ")
        attTaskName(tarefas, indiceTarefa, novoNome)

    # Completar tarefa 
    elif choose == "4":   
        viewTask(tarefas)
        indiceTarefa = input("Digite o número da tarefa que deseja marcar como completada: ")
        completeTask(tarefas, indiceTarefa)

    # Remover tarefa
    elif choose == "5": 
        deleteTask(tarefas)
        viewTask(tarefas)

    # Sair
    elif choose == "6": 
        break

print("Programa finalizado")