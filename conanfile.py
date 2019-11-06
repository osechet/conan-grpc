
import os
from conans import ConanFile, CMake, tools


class GrpcConan(ConanFile):
    """ gRPC Conan package """

    name = "gRPC"
    version = "1.12.0"
    license = "MIT"
    description = "Conan package for gRPC"
    author = "https://github.com/osechet"
    url = "https://github.com/osechet/conan-grpc"
    homepage = "https://github.com/grpc/grpc"
    topics = ("grpc", "rpc", "protobuf")
    settings = "os", "compiler", "build_type", "arch"
    requires = ("c-ares/1.15.0@conan/stable", "OpenSSL/1.1.1@conan/stable",
                "protobuf/3.6.1@bincrafters/stable", "protoc_installer/3.6.1@bincrafters/stable",
                "zlib/1.2.11@conan/stable")
    generators = "cmake"
    exports = ("LICENSE.md", "grpc.patch")

    # variables for build
    _base_name = "grpc"


    def build_requirements(self):
        self.build_requires("cmake_installer/3.13.0@conan/stable")
        if self.settings.os == "Windows":
            self.build_requires("ninja_installer/1.9.0@bincrafters/stable")


    def source(self):
        sha256 = "eb9698f23aeec2c3832601fa3f804e4d9dc28eca3cc560ef466c9ade1ec951db"
        tools.get("{0}/archive/v{1}.tar.gz".format(self.homepage, self.version), sha256=sha256)
        extracted_dir = self._base_name + "-" + self.version
        os.rename(extracted_dir, self._base_name)


    def build(self):
        tools.patch(base_path=self._base_name, patch_file="grpc.patch")

        if self.settings.os == "Windows":
            cmake = CMake(self, generator="Ninja")
        else:
            cmake = CMake(self)
        cmake.definitions["gRPC_ZLIB_PROVIDER"] = "package"
        cmake.definitions["gRPC_CARES_PROVIDER"] = "package"
        cmake.definitions["gRPC_SSL_PROVIDER"] = "package"
        cmake.definitions["gRPC_PROTOBUF_PROVIDER"] = "package"
        cmake.configure(source_dir=self._base_name)
        cmake.build()
        cmake.install()


    def package(self):
        self.copy("LICENSE", src=self._base_name, dst=".")


    def package_info(self):
        self.cpp_info.libs = [
            "gpr"
            "grpc_cronet",
            "grpc_plugin_support",
            "grpc_unsecure",
            "grpc",
            "grpc++_cronet",
            "grpc++_error_details",
            "grpc++_reflection",
            "grpc++_unsecure",
            "grpc++",
        ]
