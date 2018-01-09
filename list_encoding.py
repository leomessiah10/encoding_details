print('This program converts the string of lists into\ncoressponding numbers')

str_lst = []

def convert(lst):
    while(True):
        line = input('Enter your details \n:-')
        lst.append(line)
        choice = input('Want to enter another detail of yours\nlike email or phone number,[y/n]')
        if choice == 'y' or choice == 'Y':
            continue
        else:
            break
        return lst

convert(str_lst)

print('\nThis is your information \n',str_lst,'\n')

def encoding():
    encode = []
    count = len(str_lst)
    for me in range(count):
        code = len(str_lst[me])
        code = code *9.5
        encode.append(code)

    print('\nHere is your encoded values')
    print(encode)

encoding()

