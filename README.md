Conan package for gRPC
--------------------------------------------

[![Build Status](https://travis-ci.org/osechet/conan-grpc.svg?branch=master)](https://travis-ci.org/osechet/conan-grpc)

[![Build status](https://ci.appveyor.com/api/projects/status/fugfyh9vcv6qu60j?svg=true)](https://ci.appveyor.com/project/osechet/conan-grpc)

[ ![Download](https://api.bintray.com/packages/osechet/Conan/gRPC%3Aosechet/images/download.svg?version=1.3.7%3Atesting) ](https://bintray.com/osechet/Conan/gRPC%3Aosechet/1.3.7%3Atesting/link)

[Conan.io](https://conan.io) package for [gRPC](http://www.grpc.io/) library.

The packages generated with this **conanfile** can be found in [bintray.com](https://bintray.com/osechet/Conan/gRPC%3Aosechet).

## Reuse the package

### Basic setup

```
$ conan install gRPC/1.3.7@osechet/testing
```

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*
```
    [requires]
    gRPC/1.3.7@osechet/testing

    [options]

    [generators]
    cmake
```
Complete the installation of requirements for your project running:
```
    conan install .
```
Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.txt* and *conanbuildinfo.cmake* with all the paths and variables that you need to link with your dependencies.

## Develop the package

### Build packages

    $ pip install conan_package_tools
    $ python build.py

### Upload packages to server

    $ conan upload gRPC/1.3.7@osechet/testing --all
