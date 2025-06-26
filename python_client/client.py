import grpc
import sys
import os

# Adicione a raiz do projeto ao sys.path para importar os módulos gerados
# Assumindo que client.py está em python_client/ e tasks_pb2* estão lá
# e que python_client/ está em lista_de_tarefas_grpc/
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

# Importe os módulos gRPC gerados
# Note que eles estão no mesmo nível que client.py porque python_out=./python_client
import tasks_pb2 # O módulo gerado que contém as mensagens
import tasks_pb2_grpc # O módulo gerado que contém os stubs de cliente


def run():
    # Conecta ao servidor gRPC
    # Se o servidor estiver no mesmo PC, 'localhost:50051'
    # Se estiver em outro PC, use o IP real: '192.168.X.X:50051'
    server_address = 'localhost:50051' # Use 'localhost' para testes no mesmo PC
    # server_address = 'SEU_IP_DO_SERVIDOR:50051' # Use o IP real do PC servidor se em outra máquina
    
    # Insecure channel para simplicidade (sem SSL/TLS) para o projeto acadêmico
    with grpc.insecure_channel(server_address) as channel:
        # Cria um stub (cliente) para o serviço TaskService
        stub = tasks_pb2_grpc.TaskServiceStub(channel)

        print("===== CLIENTE gRPC DE TAREFAS =====")
        print(f"Tentando conectar ao servidor Go em {server_address}")
        # Testar a conexão com uma chamada simples, como listar tarefas
        try:
            test_request = tasks_pb2.ListTasksRequest()
            stub.ListTasks(test_request, timeout=5) # Adiciona um timeout para a conexão inicial
            print("Conexão com o servidor estabelecida com sucesso!")
        except grpc.RpcError as e:
            print(f"ERRO: Não foi possível conectar ao servidor gRPC em {server_address}. "
                  f"Verifique se o servidor está rodando e o IP/Porta estão corretos. Detalhes: {e.details}")
            sys.exit(1) # Sai se não conseguir conectar

        while True:
            print("\n===== MENU DE COMANDOS =====")
            print("1 - Criar Tarefa")
            print("2 - Listar Tarefas")
            print("3 - Atualizar Tarefa")
            print("4 - Deletar Tarefa")
            print("5 - Buscar Tarefa por ID")
            print("6 - Sair")
            
            choice = input("Escolha uma opção: ").strip()

            if choice == "1":
                title = input("Título da tarefa: ")
                description = input("Descrição da tarefa: ")
                created_by = input("Criado por (seu nome): ")
                
                if not title or not description or not created_by:
                    print("Erro: Título, descrição e criador não podem ser vazios.")
                    continue

                request = tasks_pb2.CreateTaskRequest(
                    title=title,
                    description=description,
                    created_by=created_by
                )
                try:
                    response = stub.CreateTask(request)
                    print(f"\n[RESPOSTA]: {response.message}")
                    if response.task.id:
                        print(f"Tarefa criada: ID={response.task.id}, Título='{response.task.title}'")
                except grpc.RpcError as e:
                    print(f"Erro gRPC ao criar tarefa: {e.details}")

            elif choice == "2":
                request = tasks_pb2.ListTasksRequest()
                try:
                    response = stub.ListTasks(request)
                    print(f"\n[RESPOSTA]: {response.message}")
                    if response.tasks:
                        print("--- Tarefas ---")
                        for task in response.tasks:
                            print(f"ID: {task.id}, Título: '{task.title}', Descrição: '{task.description}', Status: {task.status}, Criado por: {task.created_by}")
                        print("---------------")
                    else:
                        print("Nenhuma tarefa encontrada.")
                except grpc.RpcError as e:
                    print(f"Erro gRPC ao listar tarefas: {e.details}")

            elif choice == "3":
                try:
                    task_id = int(input("ID da tarefa para atualizar: "))
                except ValueError:
                    print("ID inválido. Por favor, digite um número.")
                    continue
                
                new_title = input("Novo título (deixe vazio para não alterar): ")
                new_description = input("Nova descrição (deixe vazio para não alterar): ")
                new_status = input("Novo status (pendente, em progresso, concluída - deixe vazio para não alterar): ")

                request = tasks_pb2.UpdateTaskRequest(id=task_id)
                # Adiciona campos apenas se não estiverem vazios
                if new_title:
                    request.title = new_title
                if new_description:
                    request.description = new_description
                if new_status:
                    request.status = new_status
                
                # Verifica se pelo menos um campo foi fornecido para atualização
                if not (new_title or new_description or new_status):
                    print("Nenhum campo fornecido para atualização. Nenhuma alteração enviada.")
                    continue

                try:
                    response = stub.UpdateTask(request)
                    print(f"\n[RESPOSTA]: {response.message}")
                    if response.task.id:
                        print(f"Tarefa atualizada: ID={response.task.id}, Título='{response.task.title}'")
                except grpc.RpcError as e:
                    print(f"Erro gRPC ao atualizar tarefa: {e.details}")

            elif choice == "4":
                try:
                    task_id = int(input("ID da tarefa para deletar: "))
                except ValueError:
                    print("ID inválido. Por favor, digite um número.")
                    continue

                request = tasks_pb2.DeleteTaskRequest(id=task_id)
                try:
                    response = stub.DeleteTask(request)
                    print(f"\n[RESPOSTA]: {response.message}")
                    if response.success:
                        print(f"Status da operação: SUCESSO")
                    else:
                        print(f"Status da operação: FALHA")
                except grpc.RpcError as e:
                    print(f"Erro gRPC ao deletar tarefa: {e.details}")

            elif choice == "5":
                try:
                    task_id = int(input("ID da tarefa para buscar: "))
                except ValueError:
                    print("ID inválido. Por favor, digite um número.")
                    continue

                request = tasks_pb2.GetTaskRequest(id=task_id)
                try:
                    response = stub.GetTask(request)
                    print(f"\n[RESPOSTA]: {response.message}")
                    if response.task.id: # Verifica se a tarefa foi realmente retornada
                        print(f"Tarefa encontrada: ID: {response.task.id}, Título: '{response.task.title}', Descrição: '{response.task.description}', Status: {response.task.status}, Criado por: {response.task.created_by}")
                    else:
                        print("Tarefa não encontrada.")
                except grpc.RpcError as e:
                    print(f"Erro gRPC ao buscar tarefa: {e.details}")

            elif choice == "6":
                print("Encerrando cliente.")
                break
            else:
                print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    run()