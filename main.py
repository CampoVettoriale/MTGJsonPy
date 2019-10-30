import json
import os
import requests

# Given a list of numbers in the input.txt file, for each number, print the card's infos.
path =os.path.dirname(__file__)
input = 'input.txt'
output = 'output.txt'
numberList = [line.rstrip('\n') for line in open(path+"/"+input)]
file_output = open(path + "/" + output, "w")
price = 0
foil_price = 0
date = "2019-10-20"
#json_set["meta"]["pricesDate"]?
#Se l'elemento della lista non è un numero, apri quel file, altrimenti cerca quel numero
for element in numberList:
    if not element.isdigit():
        json_input = element
        try:
            json_file = open(path + "/" + json_input, encoding="utf8")
            json_set = json.load(json_file)
            json_cards = json_set['cards']
            print(json_set["mcmName"])
            file_output.write(json_set["mcmName"] + "\n")
        except:
            print ("File non trovato, provo a scaricarlo?...")
            # Boh se non trovo il file provo a scaricarlo?
            # https://dzone.com/articles/simple-examples-of-downloading-files-using-python
            # https://www.mtgjson.com/json/GN2.json
            '''if len(element) == 7 or len(element) == 8:
                    try:
                        url = 'https://www.python.org/static/img/'+element;
                        print("url: "+url)
                        download = requests.get(url)
                        open(path+element, 'wb').write(download.content)
                        json_file = open(path + json_input, encoding="utf8")
                        json_set = json.load(json_file)
                        json_cards = json_set['cards']
                        print(element)
                    except:
                        print("boh non so che fare")
            else:
                print("nome sbagliato")'''
    else:
        for card in json_cards:
            if card['number'] == element:
                result = card['number'] + ": " + card['name'] + " " + card['manaCost'] + "\t\n" \
                         + card['originalType']+" "
                if "Creature" in card['originalType']:
                    result += card["power"] + "/" + card["toughness"]
                result += "\n"+card['originalText']+"\n"+str(card["prices"]["paper"]["2019-10-20"])+"$ ("+str(card["prices"]["paperFoil"]["2019-10-20"])+")$"
                price += card["prices"]["paper"][date]
                foil_price += card["prices"]["paperFoil"][date]
                print(result)
                file_output.write(result)
print("Prezzo totale:"+str(price)+"$")
print("Prezzo totale foil:"+str(foil_price)+"$")


