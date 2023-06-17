
def main():
    user_inputs = input('please input your content: ')
    convert(user_inputs)


def convert(user_inputs):
    for user_input in user_inputs:
        if user_input.isupper():
            new_user_input = "_" + user_input.lower()
            print(new_user_input, end="")
        else:
            print(user_input, end="")


main()
