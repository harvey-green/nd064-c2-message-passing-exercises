import time
from concurrent import futures

import grpc

import item_pb2
import item_pb2_grpc

import order_pb2
import order_pb2_grpc


class ItemServicer(item_pb2_grpc.ItemServiceServicer):
    def Create(self, request, context):

        request_value = {
            "name": request.name,
            "brand_name": request.brand_name,
            "id": int(request.id),
            "weight": request.weight,
        }
        print(request_value)

        return item_pb2.ItemMessage(**request_value)

class OrderServicer(order_pb2_grpc.OrderServiceServicer):
    def Create(self, request, context):

        request_value = {
            "id": request.id,
            "created_by": request.created_by,
            "status": request.status,
            "created_at": request.created_at,
            "equipment": request.equipment,
        }
        print(request_value)

        return order_pb2.OrderMessage(**request_value)

    def Get(self, request, context):

        print("got a Get orders request!")
        order1 = order_pb2.OrderMessage(
            id="100",
            created_by="Alice",
            status=0,
            created_at="2021-12-14 21:35",
            equipment=[0,1],
        )
        order2 = order_pb2.OrderMessage(
            id="101",
            created_by="Bob",
            status=0,
            created_at="2021-12-14 21:40",
            equipment=[2,3],
        )
        returnValue = {
            "orders": [order1, order2],
        }
        return order_pb2.OrderMessageList(**returnValue)




# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
item_pb2_grpc.add_ItemServiceServicer_to_server(ItemServicer(), server)
order_pb2_grpc.add_OrderServiceServicer_to_server(OrderServicer(), server)


print("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
