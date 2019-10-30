import json
# Given a list of numbers in the input.txt file, for each number, print the card's infos.
path = 'C:\\Users\\francesco.piccolo\\PycharmProjects\\MTGJsonPy\\'
input = 'input.txt'
output= 'output.txt'
numberList = [line.rstrip('\n') for line in open(path+input)]
file_output = open(path + output, "w")

#Se l'elemento della lista non è un numero, apri quel file, altrimenti cerca quel numero
for element in numberList:
    if not element.isdigit():
        json_input = element
        file_output.write(element+"\n")
        json_file = open(path + json_input, encoding="utf8")
        json_set = json.load(json_file)
        json_cards = json_set['cards']
    else:
        for targetNumber in numberList:
            for card in json_cards:
                if card['number'] == targetNumber:
                    result = card['number'] + ": " + card['name'] + " " + card['manaCost'] + "\t\n" \
                             + card['originalType']+" "
                    if "Crature" in card['originalType']:
                        result += card["power"] + "/" + card["toughness"] + "\n"
                    result += card['originalText']+"\n"
                    print(result)
                    file_output.write(result)




