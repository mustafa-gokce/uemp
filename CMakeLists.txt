cmake_minimum_required(VERSION 3.0 FATAL_ERROR)

project(UEMP CXX)

find_package(cppzmq)

add_executable(
        UEMPC
        UEMPC.cpp
)

add_executable(
        UEMPS
        UEMPS.cpp
)

find_package(cppzmq)
target_link_libraries(UEMPC cppzmq)
target_link_libraries(UEMPS cppzmq)
target_compile_features(UEMPS PRIVATE cxx_std_17)
target_compile_features(UEMPC PRIVATE cxx_std_17)