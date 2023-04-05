#include <chrono>
#include <thread>
#include <iostream>
#include <zmq.hpp>
#include <msgpack.hpp>

enum class MSG_ID : uint16_t {
    NONE = 0,
    STATE_PLAYER = 1,
    STATE_NPC = 2,
};

MSGPACK_ADD_ENUM(MSG_ID)

class MSG {
public:
    MSG_ID id{MSG_ID::NONE};
    msgpack::object msg{};
    MSGPACK_DEFINE(id, msg);
};

class STATE_PLAYER {
public:
    uint16_t id{};
    std::string name{};
    uint8_t level{};
    MSGPACK_DEFINE (id, name, level);
};

class STATE_NPC {
public:
    uint16_t id{};
    std::string name{};
    uint8_t health{};
    uint8_t strength{};
    MSGPACK_DEFINE (id, name, health, strength);
};