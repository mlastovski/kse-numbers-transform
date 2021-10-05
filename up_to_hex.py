def transform(initial_number, which_base, convert_to_base): 
    accepted = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            'A': 10,
            'B': 11,
            'C': 12,
            'D': 13,
            'E': 14,
            'F': 15
        }
    
    integer = 0

    for character in initial_number:
        value = accepted[character]
        integer *= which_base
        integer += value

    accepted = dict(map(reversed, accepted.items()))
    array = []

    while integer:
        integer, value = divmod(integer, convert_to_base)
        array.append(accepted[value])
    answer = ''.join(reversed(array))

    print(answer)


def repeat():
    ask_to_play_again = input('Try again? ^-^ Yes/No: ').lower()
    if ask_to_play_again == 'yes' or ask_to_play_again == 'no':
        return ask_to_play_again
    print('Wrong input.')


if __name__ == "__main__":
    while True:
        a = input("Please enter a number: ")
        b = int(input("Please enter the BASE that your number is in: "))
        c = int(input("Please enter the BASE TO CONVERT TO: "))
        transform(initial_number=a, which_base=b, convert_to_base=c)
    
        if repeat() == 'no':
            break
        else:
            continue
