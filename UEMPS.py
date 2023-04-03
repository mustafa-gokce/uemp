import time
import zmq
import msgpack

# create ZeroMQ server
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://127.0.0.1:6666")

# infinite loop
while True:

    # create a message object
    message = [1, [9, "mustaphos", 26]]

    # serialize the object
    serialized = msgpack.packb(message)

    # send the message with no wait
    socket.send(serialized, zmq.DONTWAIT)

    # wait for some time
    time.sleep(0.1)
