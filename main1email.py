email = 'soslyne.moreira@gmail.com'

def verify_email(email):
    prefix = True
    domain = False
    value1 = False
    value2 = True


    for a in list(email):

        if prefix:

            if value1:
                if a == '.' or a == '-' or a == '_' or a == '@' or a == '/' or a == ':':
                    value2 = False

                else:
                    value1 = False
                    continue

            elif a.isalnum():
                continue

            elif a == '.':
                value1 = True
                continue

            elif a == '-':
                value1 = True
                continue

            elif a == '_':
                value1 = True

                continue

            elif a == ':':
                value1 = True
                continue

            elif a == '/':
                value1 = True
                continue

            elif a == '@':
                prefix = False
                domain = True
                continue

            else:
                value2 = False

        elif domain:

            if a == '.':
                continue

            elif a.isalpha():
                continue

            else:
                value2 = False


    if value2 == False:
        print('The email is invalid')
    else:
        print('The email is valid')


verify_email(email)









