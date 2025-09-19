import sys

if __name__ == "__main__":
    try:
        parameter = sys.argv[1]
        if "z" in parameter:
            for i in parameter:
                if i == "z":
                    print(i, end="")
            print()
        else:
            print("none")
    except IndexError:
        print("none")
