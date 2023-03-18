import json
import random


terms = []
definitions = []
cards = {}


def action():
    action = input('Input the action (add, remove, import, export, ask, exit):\n')
    if action == 'add':
        make_cards()
    elif action == 'remove':
        remove()
    elif action == 'import':
        imprt()
    elif action == 'ask':
        check_answer()
    elif action == 'export':
        export()
    else:
        return print('Bye bye!')


def make_cards():
    global cards
    global terms
    global definitions
    term = input('The card:\n')

    while True:
        if term in terms:
            print(f'The card "{term}" already exists. Try again:')
            term = input()
        else:
            break

    definition = input('The definition of the card:\n')

    while True:
        if definition in definitions:
            print(f'The definition "{definition}" already exists. Try again:')
            definition = input()
        else:
            print(f'The pair ("{term}":"{definition}") has been added.\n')
            break

    cards[term] = definition
    terms.append(term)
    definitions.append(definition)
    return action()


def remove():
    global cards
    card_name = input('Which card?\n')
    if card_name in cards.keys():
        cards.pop(card_name)
        print('The card has been removed.\n')
        terms.remove(card_name)
        action()
    else:
        print(f"Can't remove \"{card_name}\": there is no such card.\n")
        action()


def check_answer():
    global cards
    global terms
    global definitions
    number = int(input('How many times to ask?\n'))
    for _ in range(number):
        term = random.choice(terms)
        answer = input(f'Print the definition of "{term}":\n')
        if answer == cards[term]:
            print('Correct!')
        else:
            if answer in definitions:
                print(f"Wrong. The right answer is \"{cards[term]}\", but your definition is correct for \"{list(cards.keys())[list(cards.values()).index(answer)]}\".\n")
            else:
                print(f'Wrong. The right answer is "{cards[term]}".')
    action()


def export():
    file_name = input('File name:\n')
    with open(file_name, 'a') as file:
        file.write(json.dumps(cards))
    print(f'{len(cards)} cards have been saved.\n')
    action()


def imprt():
    global cards
    file_name = input('File name:')
    try:
        with open(file_name, 'r') as file:
            cards = json.loads(file.read())
        print(f'{len(cards)} cards have been loaded.')
        action()
    except FileNotFoundError:
        print('File not found.')
        action()


def main():
    action()


if __name__ == '__main__':
    main()
