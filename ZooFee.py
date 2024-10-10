from warnings import catch_warnings

age = 0
feeSum = 0
while True:
    age = input("Enter age: ")

    if not age :
        print("your fee for zoo is", feeSum)
        break

    try:
        age = int(age)
    except:
        print("you should enter number not text!")
        continue


    if age <= 2: feeSum += 0
    elif age <= 12: feeSum += 14
    elif age >= 65: feeSum += 18
    else: feeSum += 23


