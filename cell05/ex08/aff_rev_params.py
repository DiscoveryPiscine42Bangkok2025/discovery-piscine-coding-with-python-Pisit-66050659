import sys

args = sys.argv[1:]
args = input("Enter words: ").split()
if len(args) > 2:
    for word in reversed(args):
        print(word)
else:
    print("none")