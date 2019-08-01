
import os
import subprocess
import time
from conans import ConanFile, CMake

class GdalTestConan(ConanFile):
    """ GDAL Conan package test """

    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake", "virtualenv"
    requires = "protoc_installer/3.6.1@bincrafters/stable"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        fnull = open(os.devnull, 'w')
        server = subprocess.Popen([os.sep.join([".", "bin", "greeter_server"])],
                                  stdout=fnull,
                                  stderr=subprocess.STDOUT)

        self.run(os.sep.join([".", "bin", "greeter_client"]))
        time.sleep(5)
        server.terminate()
