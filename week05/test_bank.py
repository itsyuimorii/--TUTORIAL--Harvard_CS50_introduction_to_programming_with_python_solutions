from bank import value

def test_value():
    assert value("Hello") == 0
    assert value("Hello, how are you?") == 0


    assert value("Hi") == 20
    assert value("Hey!") == 20


    assert value("What's happening?") == 100
    assert value("Goodbye") == 100

    print("All VALUE tests passed!")


if __name__ == "__main__":
    test_value()