import time
import UEMP

subscribe_socket = UEMP.create_subscribe(address="tcp://127.0.0.1:6666")

while True:
    time.sleep(1)
    data = UEMP.subscribe(socket=subscribe_socket)
    print("received:", data)
