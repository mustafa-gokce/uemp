cmake_minimum_required(VERSION 3.16.3 FATAL_ERROR)

project(UEMP CXX)

add_executable(
        UEMPC
        UEMPC.cpp
)

add_executable(
        UEMPS
        UEMPS.cpp
)

find_package(cppzmq REQUIRED)
find_package(msgpack REQUIRED)
target_link_libraries(UEMPC cppzmq msgpackc)
target_link_libraries(UEMPS cppzmq msgpackc)
target_compile_features(UEMPS PRIVATE cxx_std_11)
target_compile_features(UEMPC PRIVATE cxx_std_11)