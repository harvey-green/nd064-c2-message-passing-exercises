import time
import grpc
import item_pb2
import item_pb2_grpc
import order_pb2
import order_pb2_grpc

"""
Sample implementation of a writer that can be used to write messages to gRPC.
""" 

print("Sending sample payload...")

channel = grpc.insecure_channel("localhost:5005")

time.sleep(2)
stub = item_pb2_grpc.ItemServiceStub(channel)

# desired payload
item = item_pb2.ItemMessage(
    name="Non-Stick Frying Pan",
    brand_name="Breville",
    id=4,
    weight=4.5
)

response = stub.Create(item)

time.sleep(2)
stub2 = order_pb2_grpc.OrderServiceStub(channel)

# desired payload
order = order_pb2.OrderMessage(
    id="88",
    created_by="Harvey",
    status=0,
    created_at="2021-12-14 21:30",
    equipment=[0,1,2,3]
)


response2 = stub2.Create(order)
