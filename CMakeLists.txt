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

find_package(cppzmq)
target_link_libraries(UEMPC cppzmq)
target_link_libraries(UEMPS cppzmq)
target_compile_features(UEMPS PRIVATE cxx_std_11)
target_compile_features(UEMPC PRIVATE cxx_std_11)