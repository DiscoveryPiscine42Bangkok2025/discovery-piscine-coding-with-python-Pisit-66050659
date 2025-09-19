import sys

if __name__ == "__main__":
    try:
        print(sys.argv[1].upper())
    except IndexError:
        print("none")

