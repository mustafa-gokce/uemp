#include <chrono>
#include <thread>
#include <iostream>
#include <zmq.hpp>
#include <msgpack.hpp>

enum class MSG_ID : uint16_t {
    MSG_ID_NONE = 0,
    MSG_ID_USER = 1,
    MSG_ID_NPC = 2,
};

MSGPACK_ADD_ENUM(MSG_ID)

class MSG {
public:
    MSG_ID id{MSG_ID::MSG_ID_NONE};
    msgpack::object msg{};
    MSGPACK_DEFINE(id, msg);
};

class MSG_USER {
public:
    uint16_t id{};
    std::string name{};
    uint8_t level{};
    MSGPACK_DEFINE (id, name, level);
};

class MSG_NPC {
public:
    uint16_t id{};
    std::string name{};
    uint8_t health{};
    uint8_t strength{};
    MSGPACK_DEFINE (id, name, health, strength);
};