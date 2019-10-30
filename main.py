import json

# Given a list of numbers in the input.txt file, for each number, print the card's infos.
path = 'C:\\Users\\francesco.piccolo\\PycharmProjects\\MTGJsonPy\\'
input = 'input.txt'
json_input = 'ISD.json'
json_file = open(path + json_input, encoding="utf8")
json_set = json.load(json_file)
json_cards = json_set['cards']
print(json_cards)
