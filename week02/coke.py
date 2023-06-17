def calculate_change():
    cents = 0

    while cents != 50:
        print(f"Amount Due: {50 - cents}")
        coin = int(input("Insert Coin: "))

        if coin in [5, 10, 25]:
            cents += coin
            if cents >= 50:
                print(f"Change Owed: {cents - 50}")
                break

    return cents - 50


def main():
    change_owed = calculate_change()
    print(f"Change Owed: {abs(change_owed)}")


if __name__ == "__main__":
    main()
