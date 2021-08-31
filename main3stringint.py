

num_string = "12345"

def string_to_int(num_string):

    dictionary = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5,
                  '6' : 6, '7' : 7, '8' : 8, '9' : 9}

    #MOSTRANDO ANTES
    print(f"The valor in String: {num_string}")
    print(type(num_string))

    values= len(num_string)
    cont = 0

    for a in range(values):

        cont += dictionary[num_string[a]] * (10**(values-1-a))

    #MOSTRANDO DEPOIS
    print(f"The valor in int: {cont}")
    print(type(cont))

string_to_int(num_string)



















