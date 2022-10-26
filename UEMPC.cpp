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

        if (msg.id.id == MSG_ID::MSG_ID_USER) {
            MSG_USER msg_user;
            msg.data.convert(msg_user);
            std::cout << " [client] " << counter << " " << unsigned(msg_user.id) << " " << msg_user.name << " " << unsigned(msg_user.level) << "\n";
        } else if (msg.id.id == MSG_ID::MSG_ID_NPC) {
            MSG_NPC msg_npc;
            msg.data.convert(msg_npc);
            std::cout << " [client] " << counter << " " << unsigned(msg_npc.id) << " " << msg_npc.name << " " << unsigned(msg_npc.health) << " " << unsigned(msg_npc.strength) << "\n";
        }

        counter++;
    }
}