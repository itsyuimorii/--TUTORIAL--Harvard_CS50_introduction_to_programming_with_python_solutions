def remove_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    new_text = ""

    for char in text:
        if char not in vowels:
            new_text += char

    return new_text


def main():
    text = input("Input: ")
    result = remove_vowels(text)
    print(result)


if __name__ == "__main__":
    main()
