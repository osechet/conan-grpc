
import os
from conans import ConanFile, CMake, tools


class GrpcConan(ConanFile):
    """ gRPC Conan package """

    name = "gRPC"
    version = "1.25.0"
    license = "MIT"
    description = "Conan package for gRPC"
    author = "https://github.com/osechet"
    url = "https://github.com/osechet/conan-grpc"
    homepage = "https://github.com/grpc/grpc"
    topics = ("grpc", "rpc", "protobuf")
    settings = "os", "compiler", "build_type", "arch", "arch_build"
    requires = ("c-ares/1.15.0@conan/stable", "OpenSSL/1.1.1@conan/stable",
                "protobuf/3.9.1@bincrafters/stable",
                "zlib/1.2.11@conan/stable")
    build_requires = ("protoc_installer/3.9.1@bincrafters/stable")
    generators = "cmake"
    exports = ("LICENSE.md", "grpc.patch")

    # variables for build
    _base_name = "grpc"


    def build_requirements(self):
        self.build_requires("cmake_installer/3.13.0@conan/stable")
        if self.settings.os == "Windows":
            self.build_requires("ninja_installer/1.9.0@bincrafters/stable")


    def source(self):
        sha256 = "ffbe61269160ea745e487f79b0fd06b6edd3d50c6d9123f053b5634737cf2f69"
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
        if self.settings.arch != self.settings.arch_build:
            # To set CMAKE_SYSTEM_NAME enables cross-compilation in CMake
            cmake.definitions["CMAKE_SYSTEM_NAME"] = self.settings.os
            # If gRPC detects cross-compilation, it looks for its plugin in the prefix path.
            if os.environ.get("GRPC_INSTALL_PREFIX") is None:
                raise Exception("The path to gRPC for the build platform must be specified with the GRPC_INSTALL_PREFIX environment variable.")
            cmake.definitions["CMAKE_PREFIX_PATH"] = os.environ["GRPC_INSTALL_PREFIX"]
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
