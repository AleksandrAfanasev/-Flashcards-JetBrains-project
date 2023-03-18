def make_cards():
    cards = {}
    global terms
    global definitions
    terms = []
    definitions = []
    number_of_flashcards = int(input('Input the number of cards:\n'))
    for i in range(1, number_of_flashcards + 1):
        term = input(f'The term for card #{i}:\n')
        while True:
            if term in terms:
                print(f'The term "{term}" already exists. Try again:')
                term = input()
            else:
                break
        definition = input(f'The definition for card #{i}:\n')
        while True:
            if definition in definitions:
                print(f'The definition "{definition}" already exists. Try again:')
                definition = input()
            else:
                break
        cards[definition] = term
        terms = cards.values()
        definitions = cards.keys()
    return cards


def check_answer(cards, terms, definitions):
    for card in cards:
        answer = input(f'Print the definition of "{cards[card]}":\n')
        if answer == card:
            print('Correct!')
        else:
            if answer in definitions:
                print(f"Wrong. The right answer is \"{card}\", but your definition is correct for \"{cards[answer]}\".")
            else:
                print(f'Wrong. The right answer is "{card}".')


def main():
    check_answer(make_cards(), terms, definitions)


if __name__ == '__main__':
    main()
