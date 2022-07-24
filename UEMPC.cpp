#include "UEMPC.h"

class User {
public:
    uint32_t user_id{};
    std::string user_name{};
    uint16_t user_level{};
    MSGPACK_DEFINE (user_id, user_name, user_level);
};

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

        User user;
        msgpack::unpacked result;
        std::stringstream sbuf;
        sbuf << message.to_string();
        std::size_t off = 0;
        msgpack::unpack(result, sbuf.str().data(), sbuf.str().size(), off);
        result.get().convert(user);

        std::cout << counter << " [client] " << user.user_id << " " << user.user_name << " " << user.user_level << "\n";

        counter++;
    }

    return 0;
}