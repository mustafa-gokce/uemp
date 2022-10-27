#include "UEMPS.h"

int main(int argc, char **argv) {
    int counter = 0;

    zmq::context_t ctx;
    msgpack::zone z;
    zmq::socket_t sock(ctx, zmq::socket_type::pub);
    sock.bind("tcp://127.0.0.1:6666");

    std::this_thread::sleep_for(std::chrono::milliseconds(1000));

    while (true) {
        std::this_thread::sleep_for(std::chrono::milliseconds(100));

        MSG msg;

        if (counter % 2 == 0) {
            MSG_USER msg_user = MSG_USER{9, "warrior", 26};
            msg = MSG{MSG_ID::MSG_ID_USER, msgpack::object(msg_user, z)};
            std::cout << " [server] " << counter <<  " warrior \n";
        } else {
            MSG_NPC msg_npc = MSG_NPC{200, "salesman", 98, 100};
            msg = MSG{MSG_ID::MSG_ID_NPC, msgpack::object(msg_npc, z)};
            std::cout << " [server] " << counter <<  " salesman \n";
        }

        std::stringstream buffer;
        msgpack::pack(buffer, msg);
        const std::string payload = buffer.str();

        sock.send(zmq::buffer(payload), zmq::send_flags::dontwait);

        counter++;
    }
}