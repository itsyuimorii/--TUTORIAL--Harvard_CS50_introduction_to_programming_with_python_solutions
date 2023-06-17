def convert_camel_to_snake():
    text = input("camelCase: ")
    new_text = ""

    # loop through each character in the input text
    for i, char in enumerate(text):
        # check if the character is uppercase
        if char.isupper():
            # convert the uppercase letter to lowercase and prepend it with an underscore
            new_text += "_" + char.lower()
        else:
            new_text += char

    # print the converted snake_case text
    print(new_text)


def main():
    convert_camel_to_snake()


if __name__ == "__main__":
    main()
