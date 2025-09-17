import re

def main():
    raw_input = input('Enter text (format: "keyword" "string"): ')
    parts = raw_input.split('"')
    if len(parts) < 4:
        print("none")
        return

    keyword = parts[1].strip()
    text = parts[3].strip()

    if not keyword or not text:
        print("none")
        return

    matches = re.findall(re.escape(keyword), text)

    if matches:
        print(len(matches))
    else:
        print("none")

if __name__ == "__main__":
    main()
