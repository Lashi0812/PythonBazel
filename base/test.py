import sys
from base.level_1 import level1
from base.level_1.level_2 import level2

print(f"{__file__} with sys path {sys.path}\n")


def use():
    print(level2.level())
    print(level1.level())


if __name__ == "__main__":
    use()
