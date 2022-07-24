#include "UEMPS.h"

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
    zmq::socket_t sock(ctx, zmq::socket_type::pub);
    sock.bind("tcp://127.0.0.1:6666");

    std::this_thread::sleep_for(std::chrono::milliseconds(1000));

    while (true) {
        std::this_thread::sleep_for(std::chrono::milliseconds(100));

        User user{0, "admin", 0};
        std::stringstream buffer;
        msgpack::pack(buffer, user);
        const std::string payload = buffer.str();

        sock.send(zmq::buffer(payload), zmq::send_flags::dontwait);

        std::cout << counter << " [server] " << user.user_id << " " << user.user_name << " " << user.user_level << "\n";

        counter++;
    }

    return 0;
}