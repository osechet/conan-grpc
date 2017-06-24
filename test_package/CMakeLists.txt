# Minimum CMake required
cmake_minimum_required(VERSION 2.8)

# Project
project(HelloWorld CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

# Dependencies
find_package(gRPC REQUIRED)

# Proto file
get_filename_component(PROTO_FILE "helloworld.proto" ABSOLUTE)

# Generated sources
grpc_generate_cpp(GRPC_SRCS GRPC_HDRS ${PROTO_FILE})

# Targets greeter_[async_](client|server)
foreach(_target
        greeter_client greeter_server
        greeter_async_client greeter_async_server)
    add_executable(${_target} "${_target}.cc"
                   ${GRPC_SRCS}
                   ${GRPC_HDRS}
    )
    # Enable c++11
    target_compile_features(${_target} PRIVATE cxx_nullptr)
    target_include_directories(${_target}
        PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}
        ${CMAKE_CURRENT_BINARY_DIR}
    )
    target_link_libraries(${_target}
        PUBLIC
        gRPC::grpc++_unsecure
        gRPC::grpc++
    )
endforeach()
