def convert_emojis():
    user_input = input().strip()
    user_input_emoji = user_input.replace(":(", "🙁").replace(":)", "🙂")
    print(user_input_emoji)

if __name__ == "__main__":
    convert_emojis()