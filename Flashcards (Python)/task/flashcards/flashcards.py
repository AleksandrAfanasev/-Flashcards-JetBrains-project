def make_cards():
    cards = {}
    number_of_flashcards = int(input('Input the number of cards:\n'))
    for i in range(1, number_of_flashcards + 1):
        term = input(f'The term for card #{i}:\n')
        definition = input(f'The definition for card #{i}:\n')
        cards[definition] = term
    return cards


def check_answer(cards):
    for card in cards:
        answer = input(f'Print the definition of "{cards[card]}":\n')
        if answer == card:
            print('Correct!')
        else:
            print(f'Wrong. The right answer is "{card}".')


def main():
    check_answer(make_cards())


if __name__ == '__main__':
    main()
