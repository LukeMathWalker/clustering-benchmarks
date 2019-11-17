# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from protos import centroids_pb2 as protos_dot_centroids__pb2


class ClusteringServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Predict = channel.unary_unary(
        '/ml.ClusteringService/Predict',
        request_serializer=protos_dot_centroids__pb2.PredictRequest.SerializeToString,
        response_deserializer=protos_dot_centroids__pb2.PredictResponse.FromString,
        )
    self.PredictBatch = channel.unary_unary(
        '/ml.ClusteringService/PredictBatch',
        request_serializer=protos_dot_centroids__pb2.PredictBatchRequest.SerializeToString,
        response_deserializer=protos_dot_centroids__pb2.PredictBatchResponse.FromString,
        )


class ClusteringServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Predict(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PredictBatch(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ClusteringServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Predict': grpc.unary_unary_rpc_method_handler(
          servicer.Predict,
          request_deserializer=protos_dot_centroids__pb2.PredictRequest.FromString,
          response_serializer=protos_dot_centroids__pb2.PredictResponse.SerializeToString,
      ),
      'PredictBatch': grpc.unary_unary_rpc_method_handler(
          servicer.PredictBatch,
          request_deserializer=protos_dot_centroids__pb2.PredictBatchRequest.FromString,
          response_serializer=protos_dot_centroids__pb2.PredictBatchResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ml.ClusteringService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
