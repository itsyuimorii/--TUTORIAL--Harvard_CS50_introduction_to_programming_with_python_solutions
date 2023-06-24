class DateValidator:
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    @staticmethod
    def is_valid_date(date):
        if "/" in date:
            return DateValidator.validate_slash_date(date)
        elif "," in date:
            return DateValidator.validate_comma_date(date)
        else:
            return False

    @staticmethod
    def validate_slash_date(date):
        month, day, year = date.split("/")
        return DateValidator.is_valid_month(month) and DateValidator.is_valid_day(day) and DateValidator.is_valid_year(year)

    @staticmethod
    def validate_comma_date(date):
        date = date.replace(",", "")
        month, day, year = date.split(" ")
        return month in DateValidator.months and DateValidator.is_valid_day(day) and DateValidator.is_valid_year(year)

    @staticmethod
    def is_valid_month(month):
        try:
            month = int(month)
            return 1 <= month <= 12
        except ValueError:
            return False

    @staticmethod
    def is_valid_day(day):
        try:
            day = int(day)
            return 1 <= day <= 31
        except ValueError:
            return False

    @staticmethod
    def is_valid_year(year):
        try:
            year = int(year)
            return year >= 0
        except ValueError:
            return False


class DateConverter:
    @staticmethod
    def convert_date(date):
        year, month, day = "", "", ""

        if "/" in date:
            month, day, year = date.split("/")
        elif "," in date:
            date = date.replace(",", "")
            month, day, year = date.split(" ")

        month = int(month) if month.isdigit() else DateValidator.months.index(month) + 1

        return f"{int(year)}-{month:02}-{int(day):02}"


def main():
    while True:
        date = input("Date: ").strip()
        if DateValidator.is_valid_date(date):
            converted_date = DateConverter.convert_date(date)
            print(converted_date)
            break
        else:
            print("Invalid date. Please try again.")


main()
