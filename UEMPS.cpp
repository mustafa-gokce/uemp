#include "UEMPS.h"

int main(int argc, char **argv) {
    int counter = 0;
    zmq::context_t ctx;
    zmq::socket_t sock(ctx, zmq::socket_type::pub);
    sock.bind("tcp://127.0.0.1:6666");
    while (true) {
        zmq_sleep(1);
        const std::string payload = "{\"count\":" + std::to_string(counter) + "}";
        sock.send(zmq::buffer(payload), zmq::send_flags::dontwait);
        std::cout << "sent: " << payload << "\n";
        counter++;
    }
    return 0;
}