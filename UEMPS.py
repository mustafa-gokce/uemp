import time
import UEMP

publish_socket = UEMP.create_publish(address="tcp://127.0.0.1:6666")

i = 0
while True:
    time.sleep(1)
    data = {"count": i}
    UEMP.publish(socket=publish_socket, data=bytearray(str(data), "ascii"))
    print("sent:", data)
    i += 1
