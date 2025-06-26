package main

import (
	"context"
	"fmt"
	"log"
	"net"
	"sync"

	"google.golang.org/grpc"

	// Caminho de importação CORRETO para o seu projeto:
	// Ajustado para apontar para o sub-pacote 'pb' dentro de 'go_server'
	pb "lista_de_tarefas_grpc/go_server/pb" // <--- ATUALIZADO
)

// server é a estrutura que implementa a interface TaskServiceServer
type server struct {
	pb.UnimplementedTaskServiceServer
	tasks  []*pb.Task
	mu     sync.Mutex
	nextID int32
}

// NewServer inicializa um novo servidor de tarefas
func NewServer() *server {
	return &server{
		tasks:  make([]*pb.Task, 0),
		nextID: 1,
	}
}

// Implementação do método CreateTask
func (s *server) CreateTask(ctx context.Context, req *pb.CreateTaskRequest) (*pb.CreateTaskResponse, error) {
	s.mu.Lock()
	defer s.mu.Unlock()

	task := &pb.Task{
		Id:          s.nextID,
		Title:       req.GetTitle(),
		Description: req.GetDescription(),
		Status:      "pendente",
		CreatedBy:   req.GetCreatedBy(),
	}
	s.tasks = append(s.tasks, task)
	s.nextID++

	log.Printf("Tarefa criada: ID %d, Título: %s, Criado por: %s", task.Id, task.Title, task.CreatedBy)

	return &pb.CreateTaskResponse{
		Task:    task,
		Message: fmt.Sprintf("Tarefa '%s' criada com sucesso. ID: %d", task.Title, task.Id),
	}, nil
}

// Implementação do método ListTasks
func (s *server) ListTasks(ctx context.Context, req *pb.ListTasksRequest) (*pb.ListTasksResponse, error) {
	s.mu.Lock()
	defer s.mu.Unlock()

	return &pb.ListTasksResponse{
		Tasks:   s.tasks,
		Message: fmt.Sprintf("%d tarefas encontradas.", len(s.tasks)),
	}, nil
}

// Implementação do método UpdateTask
func (s *server) UpdateTask(ctx context.Context, req *pb.UpdateTaskRequest) (*pb.UpdateTaskResponse, error) {
	s.mu.Lock()
	defer s.mu.Unlock()

	for _, task := range s.tasks {
		if task.Id == req.GetId() {
			if req.GetTitle() != "" {
				task.Title = req.GetTitle()
			}
			if req.GetDescription() != "" {
				task.Description = req.GetDescription()
			}
			if req.GetStatus() != "" {
				task.Status = req.GetStatus()
			}
			log.Printf("Tarefa atualizada: ID %d, Novo Título: %s", task.Id, task.Title)
			return &pb.UpdateTaskResponse{
				Task:    task,
				Message: fmt.Sprintf("Tarefa ID %d atualizada com sucesso.", task.Id),
			}, nil
		}
	}

	return &pb.UpdateTaskResponse{
		Message: fmt.Sprintf("Tarefa com ID %d não encontrada.", req.GetId()),
	}, fmt.Errorf("Tarefa não encontrada")
}

// Implementação do método DeleteTask
func (s *server) DeleteTask(ctx context.Context, req *pb.DeleteTaskRequest) (*pb.DeleteTaskResponse, error) {
	s.mu.Lock()
	defer s.mu.Unlock()

	for i, task := range s.tasks {
		if task.Id == req.GetId() {
			s.tasks = append(s.tasks[:i], s.tasks[i+1:]...)
			log.Printf("Tarefa deletada: ID %d", task.Id)
			return &pb.DeleteTaskResponse{
				Success: true,
				Message: fmt.Sprintf("Tarefa ID %d deletada com sucesso.", task.Id),
			}, nil
		}
	}

	return &pb.DeleteTaskResponse{
		Success: false,
		Message: fmt.Sprintf("Tarefa com ID %d não encontrada.", req.GetId()),
	}, nil
}

// Implementação do método GetTask
func (s *server) GetTask(ctx context.Context, req *pb.GetTaskRequest) (*pb.GetTaskResponse, error) {
	s.mu.Lock()
	defer s.mu.Unlock()

	for _, task := range s.tasks {
		if task.Id == req.GetId() {
			return &pb.GetTaskResponse{
				Task:    task,
				Message: fmt.Sprintf("Tarefa ID %d encontrada.", task.Id),
			}, nil
		}
	}

	return &pb.GetTaskResponse{
		Message: fmt.Sprintf("Tarefa com ID %d não encontrada.", req.GetId()),
	}, nil
}

// Função principal para iniciar o servidor gRPC
func main() {
	port := ":50051"
	lis, err := net.Listen("tcp", port)
	if err != nil {
		log.Fatalf("Falha ao ouvir na porta %s: %v", port, err)
	}

	s := grpc.NewServer()
	pb.RegisterTaskServiceServer(s, NewServer())

	log.Printf("Servidor gRPC ouvindo em %s", port)
	if err := s.Serve(lis); err != nil {
		log.Fatalf("Falha ao iniciar servidor gRPC: %v", err)
	}
}
