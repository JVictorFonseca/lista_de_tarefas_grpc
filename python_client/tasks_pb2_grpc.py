# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import tasks_pb2 as tasks__pb2

GRPC_GENERATED_VERSION = '1.73.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in tasks_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class TaskServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateTask = channel.unary_unary(
                '/tasks.TaskService/CreateTask',
                request_serializer=tasks__pb2.CreateTaskRequest.SerializeToString,
                response_deserializer=tasks__pb2.CreateTaskResponse.FromString,
                _registered_method=True)
        self.ListTasks = channel.unary_unary(
                '/tasks.TaskService/ListTasks',
                request_serializer=tasks__pb2.ListTasksRequest.SerializeToString,
                response_deserializer=tasks__pb2.ListTasksResponse.FromString,
                _registered_method=True)
        self.UpdateTask = channel.unary_unary(
                '/tasks.TaskService/UpdateTask',
                request_serializer=tasks__pb2.UpdateTaskRequest.SerializeToString,
                response_deserializer=tasks__pb2.UpdateTaskResponse.FromString,
                _registered_method=True)
        self.DeleteTask = channel.unary_unary(
                '/tasks.TaskService/DeleteTask',
                request_serializer=tasks__pb2.DeleteTaskRequest.SerializeToString,
                response_deserializer=tasks__pb2.DeleteTaskResponse.FromString,
                _registered_method=True)
        self.GetTask = channel.unary_unary(
                '/tasks.TaskService/GetTask',
                request_serializer=tasks__pb2.GetTaskRequest.SerializeToString,
                response_deserializer=tasks__pb2.GetTaskResponse.FromString,
                _registered_method=True)


class TaskServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListTasks(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TaskServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateTask': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateTask,
                    request_deserializer=tasks__pb2.CreateTaskRequest.FromString,
                    response_serializer=tasks__pb2.CreateTaskResponse.SerializeToString,
            ),
            'ListTasks': grpc.unary_unary_rpc_method_handler(
                    servicer.ListTasks,
                    request_deserializer=tasks__pb2.ListTasksRequest.FromString,
                    response_serializer=tasks__pb2.ListTasksResponse.SerializeToString,
            ),
            'UpdateTask': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateTask,
                    request_deserializer=tasks__pb2.UpdateTaskRequest.FromString,
                    response_serializer=tasks__pb2.UpdateTaskResponse.SerializeToString,
            ),
            'DeleteTask': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteTask,
                    request_deserializer=tasks__pb2.DeleteTaskRequest.FromString,
                    response_serializer=tasks__pb2.DeleteTaskResponse.SerializeToString,
            ),
            'GetTask': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTask,
                    request_deserializer=tasks__pb2.GetTaskRequest.FromString,
                    response_serializer=tasks__pb2.GetTaskResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'tasks.TaskService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('tasks.TaskService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class TaskService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/tasks.TaskService/CreateTask',
            tasks__pb2.CreateTaskRequest.SerializeToString,
            tasks__pb2.CreateTaskResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListTasks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/tasks.TaskService/ListTasks',
            tasks__pb2.ListTasksRequest.SerializeToString,
            tasks__pb2.ListTasksResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/tasks.TaskService/UpdateTask',
            tasks__pb2.UpdateTaskRequest.SerializeToString,
            tasks__pb2.UpdateTaskResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/tasks.TaskService/DeleteTask',
            tasks__pb2.DeleteTaskRequest.SerializeToString,
            tasks__pb2.DeleteTaskResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/tasks.TaskService/GetTask',
            tasks__pb2.GetTaskRequest.SerializeToString,
            tasks__pb2.GetTaskResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
