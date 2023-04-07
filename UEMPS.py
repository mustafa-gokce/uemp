import time
import threading
import zmq
import msgpack
import UEMP

# global variables
players = {}


def publisher():
    """This function is used to create a publisher that sends messages to the subscribers"""

    # create ZeroMQ server
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://127.0.0.1:6666")

    # infinite loop
    while True:

        # send all the players
        for player in players.keys():
            # create a message object
            message = UEMP.MSG(UEMP.MSG_ID.STATE_PLAYER, players[player])

            # print the message
            # print("Server:", round(time.time(), 3), "send", message)

            # serialize the object with its method
            packed = message.pack()
            serialized = msgpack.packb(packed)

            # send the message with no wait
            socket.send(serialized, zmq.DONTWAIT)

        # wait for some time
        time.sleep(0.1)


def puller():
    """This function is used to create a puller that receives messages from the pushers"""

    # create ZeroMQ server
    context = zmq.Context()
    socket = context.socket(zmq.PULL)
    socket.bind("tcp://127.0.0.1:6667")

    # infinite loop
    while True:
        # receive the message
        serialized = socket.recv()

        # deserialize the object
        packed = msgpack.unpackb(serialized)
        message = UEMP.MSG()
        message.unpack(packed)
        player = message.msg

        # print the message
        print("Server:", round(time.time(), 3), "recv", player)

        # find the player in the list or add it if it is not there
        players[player.id] = player


def main():
    """This function is used to create the publisher and the puller"""

    # create the publisher
    publisher_thread = threading.Thread(target=publisher)
    publisher_thread.start()

    # create the puller
    puller_thread = threading.Thread(target=puller)
    puller_thread.start()

    # wait for the threads to finish
    publisher_thread.join()
    puller_thread.join()


if __name__ == "__main__":
    main()
