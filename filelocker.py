# Modules
from auth import *
import os
from pathfinder import main_path


def main():

    required_directories = ['\\files', '\\data']

    for i in required_directories:
        try:
            os.mkdir(main_path + i)
        except OSError:
            pass

    Login()


if __name__ == '__main__':
    main()
