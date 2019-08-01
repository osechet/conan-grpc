
from conans import CMake, ConanFile, tools


class GrpcConan(ConanFile):
    """ gRPC Conan package """

    name = "gRPC"
    version = "1.12.0"
    description = "Conan package for gRPC"
    license = "MIT"
    url = "https://github.com/osechet/conan-grpc"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    requires = "protobuf/3.6.1@bincrafters/stable", "OpenSSL/1.0.2l@conan/stable"
    exports = ["LICENSE.md", "FindgRPC.cmake"]


    def source(self):
        self.run("git clone -b v%s https://github.com/grpc/grpc.git" % self.version)
        with tools.chdir("grpc"):
            self.run("git submodule update --init")


    def build_requirements(self):
        if self.settings.os == "Windows":
            self.build_requires("ninja_installer/1.9.0@bincrafters/stable")


    def build_unix(self):
        """ Build on Unix systems """
        cxx_flags = []
        if self.settings.compiler.libcxx == "libstdc++":
            cxx_flags.append("-D_GLIBCXX_USE_CXX11_ABI=0")
        else:
            cxx_flags.append("-D_GLIBCXX_USE_CXX11_ABI=1")
        with tools.chdir("grpc"):
            self.run("CXXFLAGS=%s make prefix=%s install-headers install-static install-plugins" %
                     (" ".join(cxx_flags), self.package_folder))


    def build_windows(self):
        """ Build on Windows systems """
        # For MinGW, we must add -D_WIN32_WINNT=0x0600 to CXX_FLAGS
        cmake = CMake(self, generator="Ninja")
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
        self.copy("FindgRPC.cmake", src=".", dst=".")
        self.copy("LICENSE", src="grpc", dst=".")


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
        ]
