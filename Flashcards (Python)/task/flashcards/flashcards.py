term = input()
definition = input()
answer = input()

cards = {}
cards[term] = definition
if answer == cards[term]:
    print('Your answer is right!')
else:
    print('Your answer is wrong...')
