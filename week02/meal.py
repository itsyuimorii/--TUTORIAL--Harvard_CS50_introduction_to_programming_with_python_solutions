def main():
    in_time = input('What time is it? ').strip()
    time = convert(in_time)

    if 7 <= time <= 8:
        print('Breakfast time')
    elif 12 <= time <= 13:
        print('Lunch time')
    elif 18 <= time <= 19:
        print('Dinner time')


def convert(time):
    time = time.replace('a.m.', '').replace('p.m.', '')
    hours, minutes = map(int, time.split(':'))
    converted_time = hours + minutes / 60

    if 'p.m.' in time.lower() and hours != 12:
        converted_time += 12

    return round(converted_time, 2)


if __name__ == "__main__":
    main()
