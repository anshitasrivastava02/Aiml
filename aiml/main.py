def check_age(age):
    if age >= 18:
        print("Adult")
    else:
        print("Minor")


ages = [15, 18, 20]

for age in ages:
    check_age(age)