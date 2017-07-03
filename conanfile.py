
from conans import CMake, ConanFile, tools


class GrpcConan(ConanFile):
    """ gRPC Conan package """

    name = "gRPC"
    version = "1.3.7"
    description = "Conan package for gRPC"
    license = "MIT"
    url = "https://github.com/osechet/conan-grpc"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    requires = "Protobuf/3.3.1@memsharded/testing", "OpenSSL/1.0.2l@conan/stable"
    exports = "FindgRPC.cmake", "FindProtobuf.cmake"
    exports_sources = "zlib.patch"

    def configure(self):
        if self.settings.compiler == 'gcc':
            self.settings.compiler.libcxx = 'libstdc++11'

    def source(self):
        self.run("git clone -b v%s https://github.com/grpc/grpc.git" % self.version)
        self.run("cd grpc && git submodule update --init")

        if self.settings.os == "Windows":
            #self.copy("zlib.patch", ".", ".")
            # patch zlib's CMakeLists.txt
            tools.patch(base_path="grpc/third_party/zlib",
                    patch_string="""
--- a/CMakeLists.txt
+++ b/CMakeLists.txt
@@ -83,7 +83,7 @@ configure_file( ${CMAKE_CURRENT_SOURCE_DIR}/zlib.pc.cmakein
 		${ZLIB_PC} @ONLY)
 configure_file(	${CMAKE_CURRENT_SOURCE_DIR}/zconf.h.cmakein
 		${CMAKE_CURRENT_BINARY_DIR}/zconf.h @ONLY)
-include_directories(${CMAKE_CURRENT_BINARY_DIR} ${CMAKE_SOURCE_DIR})
+include_directories(${CMAKE_CURRENT_BINARY_DIR} ${CMAKE_CURRENT_SOURCE_DIR})


 #============================================================================""")

    def patch_prefix(self):
        """ patch Makefile to set the install prefix """
        tools.patch(base_path="grpc",
                    patch_string="""
--- a/Makefile
+++ b/Makefile
@@ -233,7 +233,7 @@ DEFINES_counters = NDEBUG
 # General settings.
 # You may want to change these depending on your system.

-prefix ?= /usr/local
+prefix ?= %s

 PROTOC ?= protoc
 DTRACE ?= dtrace""" % self.package_folder)

    def build_unix(self):
        """ Build on Unix systems """
        self.patch_prefix()
        self.run("cd grpc && make install-headers install-static install-plugins")

    def build_windows(self):
        """ Build on Windows systems """
        cmake = CMake(self)
        cmake.definitions["CMAKE_INSTALL_PREFIX"] = self.package_folder
        cmake.configure(source_dir="grpc")
        cmake.build()
        cmake.build(target="install")

    def build(self):
        if self.settings.os == "Windows":
            self.build_windows()
        else:
            self.build_unix()

    def package(self):
        self.copy("FindProtobuf.cmake", ".", ".")
        self.copy("FindgRPC.cmake", ".", ".")

    def package_info(self):
        self.cpp_info.libs = [
            "gpr"
            "grpc",
            "grpc++",
            "grpc++_cronet",
            "grpc++_error_details",
            "grpc++_reflection",
            "grpc++_unsecure",
            "grpc_cronet",
            "grpc_unsecure",
            "grpc_unsecure"
        ]
