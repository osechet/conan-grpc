
from conan.packager import ConanMultiPackager

def main():
    """ Main function """

    builder = ConanMultiPackager()
    builder.add_common_builds(pure_c=False)
    builder.run()

if __name__ == "__main__":
    main()
