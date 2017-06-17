
import os
import subprocess
import time
from conans import ConanFile, CMake

# This easily allows to copy the package in other user or channel
CHANNEL = os.getenv("CONAN_CHANNEL", "testing")
USERNAME = os.getenv("CONAN_USERNAME", "osechet")

class GRPCTestConan(ConanFile):
    """ gRPC Conan package test """

    requires = "gRPC/1.3.7@%s/%s" % (USERNAME, CHANNEL)
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake "%s" %s' % (self.conanfile_directory, cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)

    def test(self):
        fnull = open(os.devnull, 'w')
        server = subprocess.Popen([os.sep.join([".", "bin", "greeter_server"])],
                                  stdout=fnull,
                                  stderr=subprocess.STDOUT)

        self.run("%s" % (os.sep.join([".", "bin", "greeter_client"])))
        time.sleep(5)
        server.terminate()
