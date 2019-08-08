cmake_minimum_required(VERSION 2.8.12)

# Project
project(HelloWorld)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

# Dependencies
find_package(gRPC REQUIRED)

# Proto file
get_filename_component(PROTO_FILE "helloworld.proto" ABSOLUTE)

if (MSVC)
    add_definitions(-D_WIN32_WINNT=0x600)
endif()

# Generated sources
protobuf_generate_cpp(PROTO_SRCS PROTO_HDRS ${PROTO_FILE})
grpc_generate_cpp(GRPC_SRCS GRPC_HDRS ${PROTO_FILE})
# protobuf_generate_python(PYTHON_PROTO_SRCS ${PROTO_FILE})
# grpc_generate_python(PYTHON_GRPC_SRCS ${PROTO_FILE})
# add_custom_target(GenPython ALL
#                   DEPENDS ${PYTHON_GRPC_SRCS} ${PYTHON_PROTO_SRCS})

# Targets greeter_[async_](client|server)
foreach(_target
        greeter_client greeter_server
        greeter_async_client greeter_async_server)
    add_executable(${_target} "${_target}.cc"
                   ${PROTO_SRCS} ${PROTO_HDRS}
                   ${GRPC_SRCS} ${GRPC_HDRS}
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
    )
endforeach()
