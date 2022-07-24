import zmq


# publish to endpoints
def publish(socket, data):
    return socket.send(data)


# subscribe in endpoints
def subscribe(socket):
    data = socket.recv()
    return data


# create pub socket
def create_publish(address):
    pub_context = zmq.Context()
    pub_socket = pub_context.socket(zmq.PUB)
    pub_socket.bind(address)
    return pub_socket


# create sub socket
def create_subscribe(address):
    sub_context = zmq.Context()
    sub_socket = sub_context.socket(zmq.SUB)
    sub_socket.setsockopt(zmq.SUBSCRIBE, b"")
    sub_socket.connect(address)
    return sub_socket
