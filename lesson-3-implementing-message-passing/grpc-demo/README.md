## Generating gRPC files
`pip install grpcio-tools grpcio`

`python3 -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ item.proto`

`python3 -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ order.proto`