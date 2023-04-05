#include "UEMPC.h"

int main(int argc, char **argv) {
    int counter = 0;

    zmq::context_t ctx;
    zmq::socket_t sock(ctx, zmq::socket_type::sub);
    sock.connect("tcp://127.0.0.1:6666");
    sock.set(zmq::sockopt::subscribe, "");

    std::this_thread::sleep_for(std::chrono::milliseconds(1000));

    while (true) {
        std::this_thread::sleep_for(std::chrono::milliseconds(100));

        zmq::message_t message;
        (void) sock.recv(message);

        MSG msg;
        msgpack::unpacked result;
        std::stringstream sbuf;
        sbuf << message.to_string();
        std::size_t off = 0;
        msgpack::unpack(result, sbuf.str().data(), sbuf.str().size(), off);
        result.get().convert(msg);

        try {
            if (msg.id == MSG_ID::STATE_PLAYER) {
                STATE_PLAYER state_player;
                msg.msg.convert(state_player);
                std::cout << " [client] " << counter << " " << unsigned(state_player.id) << " " << state_player.name << " " << unsigned(state_player.level) << "\n";
            } else if (msg.id == MSG_ID::STATE_NPC) {
                STATE_NPC state_npc;
                msg.msg.convert(state_npc);
                std::cout << " [client] " << counter << " " << unsigned(state_npc.id) << " " << state_npc.name << " " << unsigned(state_npc.health) << " " << unsigned(state_npc.strength) << "\n";
            }
        } catch (const std::exception &e) {
            std::cout << " [client] " << counter << " " << e.what() << "\n";
        }

        counter++;
    }
}