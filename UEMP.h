#include <chrono>
#include <thread>
#include <iostream>
#include <zmq.hpp>
#include <msgpack.hpp>
#include <boost/filesystem.hpp>

enum class MSG_ID : uint16_t {
    MSG_ID_NONE = 0,
    MSG_ID_USER = 1,
    MSG_ID_NPC = 2,
};

union msg_id_t {
    MSG_ID      id;
    uint16_t    id_int;
};

struct MSG {
    msg_id_t id{MSG_ID::MSG_ID_NONE};
    msgpack::object data{};
    MSGPACK_DEFINE(id.id_int, data);
};

struct MSG_USER {
    uint16_t id{};
    std::string name{};
    uint8_t level{};
    MSGPACK_DEFINE (id, name, level);
};

struct MSG_NPC {
    uint16_t id{};
    std::string name{};
    uint8_t health{};
    uint8_t strength{};
    MSGPACK_DEFINE (id, name, health, strength);
};