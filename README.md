# lista_de_tarefas_grpc# 🚀 Gerenciador de Tarefas Distribuído (gRPC com Go e Python) 🚀

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Go](https://img.shields.io/badge/Go-1.22%2B-blue.svg)
![gRPC](https://img.shields.io/badge/gRPC-Framework-green.svg)
![Protocol Buffers](https://img.shields.io/badge/Protocol%20Buffers-Data-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg) ## 📝 Visão Geral do Projeto

Este projeto demonstra a implementação de um **Gerenciador de Tarefas Distribuído** utilizando **gRPC** para a comunicação entre serviços em duas linguagens de programação distintas: **Go (servidor)** e **Python (cliente)**. Ele permite a criação, listagem, atualização, exclusão e busca de tarefas remotamente, servindo como um estudo de caso para a **transmissão de dados de alto desempenho e tipagem forte** com gRPC.

As tarefas são armazenadas temporariamente na memória do servidor (não há persistência em banco de dados neste exemplo).

## ✨ Funcionalidades

* **Criação de Tarefas:** Adicione novas tarefas com título, descrição e criador.
* **Listagem de Tarefas:** Visualize todas as tarefas existentes no sistema.
* **Atualização de Tarefas:** Modifique título, descrição ou status de tarefas por ID.
* **Exclusão de Tarefas:** Remova tarefas existentes por ID.
* **Busca de Tarefa:** Encontre uma tarefa específica pelo seu ID.

## 📐 Arquitetura do Sistema

A arquitetura do projeto segue um modelo cliente-servidor, onde a comunicação é feita exclusivamente via gRPC.

+-------------------+                          +-------------------+
|                   |                          |                   |
|  Cliente Python   |<------ gRPC RPCs ------>|     Servidor Go   |
|  (Interface CLI)  |       (HTTP/2 + Protobuf)  |  (Lógica de Tarefas)  |
|                   |                          |                   |
+-------------------+                          +-------------------+
^                                            ^
|                                            |
|  python_client/client.py                 |  go_server/main.go
|  python_client/tasks_pb2*.py             |  go_server/pb/tasks_pb*.go
|                                            |
+--------------------------------------------+
tasks.proto (Contrato de Serviço)


-   **`tasks.proto`**: Define o contrato de serviço (mensagens e métodos RPC) compartilhado entre cliente e servidor.
-   **Servidor Go (`go_server/`)**: Implementa o serviço `TaskService` definido no `.proto`, gerencia a lista de tarefas em memória e expõe a API gRPC.
-   **Cliente Python (`python_client/`)**: Utiliza o stub gRPC gerado para chamar os métodos do servidor Go e interage com o usuário através de uma interface de linha de comando.

## 🛠️ Tecnologias Utilizadas

* **Linguagens:** Python (v3.8+) e Go (v1.22+)
* **Framework RPC:** gRPC
* **Serialização de Dados:** Protocol Buffers (Protobuf)
* **Controle de Versão:** Git / GitHub
* **Ambiente de Desenvolvimento:** Visual Studio Code

## 🚀 Como Rodar o Projeto

Siga estes passos para configurar e executar o servidor e o cliente em sua máquina.

### Pré-requisitos

Certifique-se de ter instalado em sua máquina:

* [**Git**](https://git-scm.com/downloads)
* [**Python 3.8+**](https://www.python.org/downloads/) (com `pip` configurado)
* [**Go 1.22+**](https://go.dev/dl/)
* [**Compilador `protoc`**](https://github.com/protocolbuffers/protobuf/releases) (baixe a versão `win64.zip` e adicione a pasta `bin` ao seu PATH do sistema)

### 1. Clonar o Repositório

Abra seu terminal (ou Prompt de Comando/PowerShell) e execute:

```bash
git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git) cd SEU_REPOSITORIO_CLONADO ```

### 2. Instalar Ferramentas e Gerar Código gRPC

Abra o **Visual Studio Code** na pasta raiz do projeto (`SEU_REPOSITORIO_CLONADO`). Abra o terminal integrado do VS Code (`Terminal` -> `New Terminal`).

#### a. Instalar Ferramentas Go e Python gRPC

Na **raiz do projeto**, execute:

```bash
# Para Go
go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest

# Para Python
pip install grpcio grpcio-tools
b. Gerar Arquivos .pb.go e .pb2.py
Crie a pasta go_server/pb se ela não existir.

Na raiz do projeto, execute os comandos protoc manualmente (se as VS Code Tasks não funcionarem):

Bash

# Para Go
protoc --go_out=./go_server/pb --go_opt=paths=source_relative --go-grpc_out=./go_server/pb --go-grpc_opt=paths=source_relative tasks.proto

# Para Python
python -m grpc_tools.protoc -I. --python_out=./python_client --grpc_python_out=./python_client tasks.proto
Alternativa: Gerar via VS Code Tasks (se configurado)
c. Inicializar e Organizar Módulo Go
Na raiz do projeto, execute:

Bash

go mod init lista_de_tarefas_grpc
go mod tidy
3. Executar o Servidor Go
⚠️ ATENÇÃO: CONFIGURAÇÃO DE FIREWALL ⚠️
Se você estiver rodando o servidor em um PC e o cliente em outro, ou se o cliente não conseguir conectar (Tempo limite de conexão esgotado), é CRUCIAL que você permita o python.exe e o go.exe (ou o executável gerado pelo Go) através do firewall do Windows Defender na máquina do servidor (portas TCP/UDP 50051).

Abra um terminal na raiz do seu projeto.

Execute o servidor Go:

Bash

go run go_server/main.go
Você verá a mensagem: Servidor gRPC ouvindo em :50051. Deixe este terminal aberto.

4. Executar o Cliente Python
Abra outro terminal (ou Prompt de Comando/PowerShell).

Navegue até a pasta do cliente:

cd python_client
Execute o cliente Python:


python client.py
O cliente iniciará e exibirá um menu interativo.

⚠️ ATENÇÃO: IP DO SERVIDOR ⚠️
No código python_client/client.py, a variável server_address está configurada como 'localhost:50051'. Se o servidor Go estiver rodando em outro computador na sua rede, você precisará editar essa linha no client.py para o IP real do computador do servidor (ex: '192.168.1.100:50051').

🎮 Como Usar (Interação com o Cliente)
Após iniciar o cliente Python, use as opções do menu para interagir:

1 - Criar Tarefa: Digite título, descrição e seu nome.

2 - Listar Tarefas: Veja todas as tarefas criadas.

3 - Atualizar Tarefa: Informe o ID e os novos dados.

4 - Deletar Tarefa: Informe o ID.

5 - Buscar Tarefa por ID: Informe o ID para ver detalhes.

6 - Sair: Encerra o cliente.

Observe os logs em ambos os terminais (servidor e cliente) para ver a comunicação gRPC em ação!

💡 Próximas Melhorias Possíveis
Persistência de Dados: Salvar tarefas em um arquivo (JSON/SQLite) ou banco de dados real (PostgreSQL, MySQL).

Interface Gráfica (GUI) para o Cliente Python: Usar Tkinter, PyQt ou Kivy para uma experiência de usuário mais rica.

Autenticação e Autorização: Implementar login de usuários e controle de acesso às tarefas.

Testes Unitários e de Integração: Adicionar testes para o servidor e o cliente.

Deployment: Empacotar a aplicação para distribuição (executáveis, contêineres Docker).

🤝 Contribuições
Contribuições são bem-vindas! Se tiver sugestões ou melhorias, sinta-se à vontade para abrir uma issue ou enviar um Pull Request.

📄 Licença
Este projeto está licenciado sob a Licença MIT.

Desenvolvido por: [Seu Nome/GitHub] Data: [Dia Mês, Ano] ```