import time
import zmq
import msgpack
import UEMP

# create ZeroMQ server
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://127.0.0.1:6666")

# initialize counter
i = -1

# infinite loop
while True:

    # increment counter
    i += 1

    # create user message
    if i % 2 == 0:

        # create a message object
        message = UEMP.MSG(UEMP.MSG_ID.STATE_PLAYER, UEMP.STATE_PLAYER(9, "mustaphos", 26))

    # create npc message
    else:

        # create a message object
        message = UEMP.MSG(UEMP.MSG_ID.STATE_NPC, UEMP.STATE_NPC(13, "depocu", 26, 10))

    # print the message
    print(i, message)

    # serialize the object with its method
    packed = message.pack()
    serialized = msgpack.packb(packed)

    # send the message with no wait
    socket.send(serialized, zmq.DONTWAIT)

    # wait for some time
    time.sleep(0.1)
