import json
# Given a list of numbers in the input.txt file, for each number, print the card's infos.
path = 'C:\\Users\\francesco.piccolo\\PycharmProjects\\MTGJsonPy\\'
input = 'input.txt'
numberList = [line.rstrip('\n') for line in open(path+input)]
json_input = 'ISD.json'
json_file = open(path + json_input, encoding="utf8")
json_set = json.load(json_file)
json_cards = json_set['cards']
for targetNumber in numberList:
    for card in json_cards:
        if card['number'] == targetNumber:
            print(card['number']+": "+card['name']+" "+card['manaCost'])




