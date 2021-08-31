dates = '05//04/1996'

def verify_date(dates):
    day = True
    month = False
    year = False
    value1 = True
    cont = 0

    for a in list(dates):
        if day:

            if cont > 2:
                value1 = False


            elif a.isnumeric():
                cont += 1
                continue

            elif a == "/":
                day = False
                month = True
                cont = 0
                continue

            else:
                value1 = False

        elif month:

            if cont > 2:
                value1 = False

            elif a.isnumeric():
                cont += 1
                continue

            elif a == "/":
                month = False
                year = True
                cont = 0
                continue

            else:
                value1 = False

        elif year:
            if cont >= 4:
                value1 = False

            elif a.isnumeric():
                cont += 1
                continue

            else:
                value1 = False

    if value1 == False:
        print('The date is invalid')
    else:
        print('The date is valid')

verify_date(dates)