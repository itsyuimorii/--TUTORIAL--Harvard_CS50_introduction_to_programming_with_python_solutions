def is_valid_length(s):
    return 2 <= len(s) <= 6


def is_valid_alphanumeric(s):
    return s.isalnum()


def is_valid_first_characters(s):
    return s[0].isalpha() and s[1].isalpha()


def is_valid_first_number(s):
    for character in s:
        if character.isnumeric():
            if character == '0':
                return False
            break
    return True


def is_valid_no_alphabet_after_first_number(s):
    first_num = len(s) - 1
    for i, character in enumerate(s):
        if character.isnumeric():
            first_num = i
            break
    for character in s[first_num + 1:]:
        if character.isalpha():
            return False
    return True


def is_valid(s):
    return (
        is_valid_length(s) and
        is_valid_alphanumeric(s) and
        is_valid_first_characters(s) and
        is_valid_first_number(s) and
        is_valid_no_alphabet_after_first_number(s)
    )


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
