def sort_grocery_list(grocery_list):
    sorted_items = dict(sorted(grocery_list.items()))

    for item, count in sorted_items.items():
        print(count, item)


def main():
    grocery_list = {}

    while True:
        try:
            item = input().upper()
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1
        except EOFError:
            sort_grocery_list(grocery_list)
            break


if __name__ == "__main__":
    main()
