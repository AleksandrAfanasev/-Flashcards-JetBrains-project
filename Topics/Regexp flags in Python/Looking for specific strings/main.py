import re

string = input()
print(string if re.match('^b|.*l$', string, re.IGNORECASE) else 'No match')
