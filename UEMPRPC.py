import argparse
import random
import time
import zmq


def server():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")
    time.sleep(1)
    while True:
        msg = socket.recv_json()
        print("Server Got:  ", msg)
        result = eval("{}{}{}".format(msg["first"], msg["operation"], msg["second"]))
        data = {"client_id": msg["client_id"], "result": result}
        socket.send_json(data)
        print("Server Sent: ", data)


def client(client_id):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")
    time.sleep(1)
    while True:
        data = {"client_id": client_id,
                "first": random.randint(1, 100),
                "second": random.randint(1, 100),
                "operation": random.choice(["+", "-", "*", "/"])}
        socket.send_json(data)
        print("Client Sent: ", data)
        msg = socket.recv_json()
        print("Client Got:  ", msg)
        time.sleep(random.randint(1, 5))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--client", action="store_true", help="Run as client")
    parser.add_argument("-i", "--id", type=int, default=1, help="Client ID")
    args = parser.parse_args()

    print("Running as client" if args.client else "Running as server")
    print(f"Client ID: {args.id}" if args.client else "")

    if args.client:
        client(args.id)
    else:
        server()
