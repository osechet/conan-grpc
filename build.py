
from conan.packager import ConanMultiPackager

def main():
    """ Main function """

    builder = ConanMultiPackager()
    builder.add_common_builds(pure_c=False)
    builder.remove_build_if(lambda build: build.settings["arch"] != "x86_64")
    builder.run()

if __name__ == "__main__":
    main()
