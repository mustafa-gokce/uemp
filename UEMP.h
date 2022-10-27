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

class MSG {
public:
    MSG_ID id{MSG_ID::MSG_ID_NONE};
    msgpack::object data{};
    MSGPACK_DEFINE((uint16_t&)id, data);
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