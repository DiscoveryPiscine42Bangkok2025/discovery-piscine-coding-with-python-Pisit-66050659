import sys

if __name__ == "__main__":
    if len(sys.argv[1:]) > 0:
        print(f"Parameters: {len(sys.argv[1:])}")
        for i in sys.argv[1:]:
            print(f"{i}: {len(i)}")
    else:
        print("none")
