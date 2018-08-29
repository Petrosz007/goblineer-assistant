import text_to_speech as tts
import get_data
import sys
from num2words import num2words
from math import trunc
import re
import webbrowser


mv_names = get_data.load_json("https://goblineer.tk/json/mv_names.json")

def run_without_mic(): 
    while True:
        item_to_search = input("Item to search: ")
        found = False

        if item_to_search == "exit":
            sys.exit()

        for data in mv_names:
            if data["name"].upper() == item_to_search.upper():
                marketvalue = float(data["marketvalue"])
                marketvalue_gold = trunc(marketvalue)
                marketvalue_silver = trunc(round(marketvalue - marketvalue_gold, 2) * 100)

                tts.say("The marketvalue of " + data["name"] + " is " + num2words(marketvalue_gold) + " gold and " + num2words(marketvalue_silver) + " silver")
                found = True
                break

        if not found:
            tts.say("Item not found.")

def get_marketvalue(item_to_search):
    found = False

    for data in mv_names:
        if data["name"].upper() == item_to_search.upper():
            marketvalue = float(data["marketvalue"])
            marketvalue_gold = trunc(marketvalue)
            marketvalue_silver = trunc(round(marketvalue - marketvalue_gold, 2) * 100)

            tts.say("The marketvalue of " + data["name"] + " is " + num2words(marketvalue_gold) + " gold and " + num2words(marketvalue_silver) + " silver")
            found = True
            break

    if not found:
        tts.say("Item not found.")

def get_quantity(item_to_search):
    found = False

    for data in mv_names:
        if data["name"].upper() == item_to_search.upper():
            quantity = data["quantity"]

            tts.say("The quantity of " + data["name"] + " is " + num2words(quantity))
            found = True
            break

    if not found:
        tts.say("Item not found.")

def assistant(command):
    if "price of" in command:
        regex = re.search("price of (.*)", command)
        if regex:
            item = regex.group(1)
            get_marketvalue(item)
        print("Done!")

    if "quantity of" in command:
        regex = re.search("quantity of (.*)", command)
        if regex:
            item = regex.group(1)
            get_quantity(item)
        print("Done!")
    
    if "show me" in command:
        regex = re.search("show me (.*)", command)
        if regex:
            item = regex.group(1)
            webbrowser.open("https://goblineer.tk/item/" + item.replace(" ", "+"))
        print("Done!")

    if "exit" == command:
        tts.say("Goodbye!")
        sys.exit()

    if "dog" in command:
        webbrowser.open(get_data.load_json("https://dog.ceo/api/breeds/image/random")["message"])

    return