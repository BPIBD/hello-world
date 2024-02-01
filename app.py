import time
alphabets = "abcdefghijklmnopqrstuvwxyz"
text = "hello world"
found = ""

for char in text:
    # print(char)
    if char == " ":
        found += char
        continue

    for c in alphabets:
        time.sleep(0.02)
        print(f"{found}{c}")
        if c == char:
            found += c
            break
