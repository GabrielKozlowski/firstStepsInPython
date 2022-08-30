from datetime import date


def calculates_how_much_time_is_alive(day, month, year):
    timeToday = date.today()
    timeLeft = []
    day = (timeToday.day - int(day))
    timeLeft.append(abs(day))
    month = (timeToday.month - int(month))
    timeLeft.append(abs(month))
    year = (timeToday.year - int(year))
    timeLeft.append(year)
    return timeLeft


def get_answer_how_long_time_live_on_earth():
    while True:
        question = input(
            "Hello want you know how long you lives in earth ?? yes or no: ")
        if (question == 'yes'):
            dayOfBirtday = input("What is your day of birtday? : ")
            monthOfBirtday = input("Your month? : ")
            yearOfBirtday = input("And the year? : ")
            howLongSomeoneLives = calculates_how_much_time_is_alive(
                dayOfBirtday, monthOfBirtday, yearOfBirtday)
            print("You are already alive : ", howLongSomeoneLives[0], "Days", howLongSomeoneLives[1],
                  "Month", howLongSomeoneLives[2], "Years")
            break
        elif (question == 'no'):
            print("Ok goodbye ")
            break
        else:
            print("Only yes or no answers !")
            continue


def get_how_many_days_have_passed_since_birth(day, month, year):
    timeToday = date.today()
    dateOfBirth = date(year, month, day)
    passedDays = (timeToday - dateOfBirth)
    answer = print("Days have passed since birthday: ", passedDays)
    return answer


get_how_many_days_have_passed_since_birth(30, 1, 1989)


