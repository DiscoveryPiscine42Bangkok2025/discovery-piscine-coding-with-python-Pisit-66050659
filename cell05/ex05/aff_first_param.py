import sys
args = sys.argv[1:]
args = input("Enter words: ").split()
if len(args) > 0:
    print(args[0])
else:
    print("none")