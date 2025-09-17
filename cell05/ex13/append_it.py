def main():
    args = input("Enter words: ").split()

    if not args:
        print("none")
    else:
        for word in args:
            if word.endswith("ism"):
                continue
            print(word + "ism")
if __name__ == "__main__":
    main()