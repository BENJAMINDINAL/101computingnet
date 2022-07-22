code = input()


def egg(code):

    if code[0] == '0':
        print("Organic egg")
    elif code[0]== '1':
        print("Free Range egg")
    elif code[0] == '2':
        print("Barn egg")
    elif code[0] == '3':
        print("Cage egg")

    dictionary = {}



    with open('country-codes.txt', 'r') as f:
        for line in f:
            (key ,value) = line.split(',', 1)
            dictionary[key] = value


    print("Country of Origin: "),
    str(code)
    print(dictionary.get(code[1:3]))
    print("Farm Id: "),
    print(code[3:])

if len(code) > 8:
    print("this is wrong")
elif int(code[0]) > 3:
    print("this is wrong")
else:
    egg(code)