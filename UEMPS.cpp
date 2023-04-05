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
            STATE_PLAYER state_player = STATE_PLAYER{9, "warrior", 26};
            msg = MSG{MSG_ID::STATE_PLAYER, msgpack::object(state_player, z)};
            std::cout << " [server] " << counter <<  " warrior \n";
        } else {
            STATE_NPC state_npc = STATE_NPC{200, "salesman", 98, 100};
            msg = MSG{MSG_ID::STATE_NPC, msgpack::object(state_npc, z)};
            std::cout << " [server] " << counter <<  " salesman \n";
        }

        std::stringstream buffer;
        msgpack::pack(buffer, msg);
        const std::string payload = buffer.str();

        sock.send(zmq::buffer(payload), zmq::send_flags::dontwait);

        counter++;
    }
}