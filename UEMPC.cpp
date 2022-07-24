#include "UEMPC.h"

int main(int argc, char **argv) {
    int counter = 0;
    zmq::context_t ctx;
    zmq::socket_t sock(ctx, zmq::socket_type::sub);
    sock.connect("tcp://127.0.0.1:6666");
    sock.set(zmq::sockopt::subscribe, "");
    while (true) {
        zmq_sleep(1);
        zmq::message_t message;
        (void) sock.recv(message);
        std::string recv_msg(message.data<char>(), message.size());
        std::cout << "received: " << message.to_string() << "\n";
        counter++;
    }
    return 0;
}