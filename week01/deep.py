user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
answer = user_input.lower().strip()
if (answer == "42" or answer == "forty-two" or answer == "forty two"):
    print("Yes")
else:
    print("no")