import sys
import time
import threading
import random
import zmq
import msgpack
import UEMP


def subscriber():
    """This function is used to create a subscriber that receives messages from the publisher"""

    # create ZeroMQ client
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://127.0.0.1:6666")
    socket.setsockopt(zmq.SUBSCRIBE, b"")

    # infinite loop
    while True:
        # receive the message
        serialized = socket.recv()

        # deserialize the message
        packed = msgpack.unpackb(serialized)
        print(packed)
        message = UEMP.MSG()
        message.unpack(packed)

        # print the message
        print("Client:", round(time.time(), 3), "recv", message)


def pusher(instance):
    """This function is used to create a pusher that sends messages to the puller"""

    # create ZeroMQ client
    context = zmq.Context()
    socket = context.socket(zmq.PUSH)
    socket.connect("tcp://127.0.0.1:6667")

    # infinite loop
    while True:
        # create a message object
        message = UEMP.MSG(UEMP.MSG_ID.STATE_PLAYER,
                           UEMP.STATE_PLAYER(instance, f"Player {instance}", random.randint(0, 100)))

        # print the message
        # print("Client:", round(time.time(), 3), "send", message)

        # serialize the object with its method
        packed = message.pack()
        serialized = msgpack.packb(packed)

        # send the message with no wait
        socket.send(serialized, zmq.DONTWAIT)

        # wait for some time
        time.sleep(0.1)


def main():
    """This function is used to create the subscriber and the pusher"""

    # get input arguments
    instance = sys.argv[1]

    # create the subscriber
    subscriber_thread = threading.Thread(target=subscriber)
    subscriber_thread.start()

    # create the pusher
    pusher_thread = threading.Thread(target=pusher, args=(instance,))
    pusher_thread.start()

    # wait for the threads to finish
    subscriber_thread.join()
    pusher_thread.join()


if __name__ == "__main__":
    main()
