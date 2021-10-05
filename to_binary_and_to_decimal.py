def transform(x, user_input):
    output = ''

    if x == 2: 
        user_input = int(user_input)
        while user_input != 0:
            number = user_input % 2
            output = str(number) + output
            user_input = int(user_input) // 2
        output = '0b' + output
        print(output)
    
    elif x == 10:
        j = len(user_input) - 3
        n = 0
        for i in range(2, len(user_input)):
            n += int(user_input[i]) * (2 ** j)
            j -= 1
        print(n)


def repeat():
    while True:
        answer = input('Try again? ^-^ Yes/No: ').lower()
        if answer == 'yes' or answer == 'no':
            return answer
        print('Wrong input.')


if __name__ == "__main__":
    while True:
        user_input = input('Enter your number in decimal or binary format: ')

        if user_input[:2] == '0b':
            for i in user_input[2:]:
                if int(i) != 1 and int(i) != 0:
                    print('wrong input')
                    exit()
            x = 10

        else:
            for i in user_input:
                if not i.isdigit():
                    print('йоу, козаче, не всі блін числа')
                    exit()
            x = 2

        transform(x, user_input)

        if repeat() == 'no':
            break
        else:
            continue
