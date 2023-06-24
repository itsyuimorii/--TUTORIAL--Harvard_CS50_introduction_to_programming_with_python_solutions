def get_valid_fraction():
    while True:
        try:
            numerator, denominator = input("Fraction: ").split("/")
            numerator, denominator = int(numerator), int(denominator)
            if denominator < numerator:
                raise Exception
            elif denominator == 0:
                raise ZeroDivisionError
        except:
            pass
        else:
            return numerator, denominator

def calculate_grade(numerator, denominator):
    percent = (numerator / denominator) * 100
    if percent <= 1:
        return 'E'
    elif percent >= 99:
        return 'F'
    else:
        return f'{percent:.0f}%'

numerator, denominator = get_valid_fraction()
result = calculate_grade(numerator, denominator)
print(result)
