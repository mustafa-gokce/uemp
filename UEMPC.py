import time
import zmq
import msgpack
import UEMP

# create ZeroMQ client
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://127.0.0.1:6666")
socket.setsockopt(zmq.SUBSCRIBE, b"")

# initialize counter
i = -1

# infinite loop
while True:

    # increment counter
    i += 1

    # receive the message
    serialized = socket.recv()

    # deserialize the message
    packed = msgpack.unpackb(serialized)
    message = UEMP.MSG()
    message.unpack(packed)

    # print the message
    print(i, message)
