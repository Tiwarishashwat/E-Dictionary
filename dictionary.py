import json
import difflib
import time
from difflib import SequenceMatcher
from difflib import get_close_matches
data = json.load(open("data.json"))
key=input("what you want to search?\n")
def get(key):
    key=key.lower()
    if key in data:
        return data[key]
    elif key.title() in data:
        return data[key.title()]
    elif key.upper() in data:
        return data[key.upper()]
    elif len(get_close_matches(key,data.keys())) > 0:
        yn=input("Did you mean %s instead\n Enter Y if yes or N if no\n" %get_close_matches(key,data.keys())[0])
        if yn=='Y' or yn=='y':
            return data[get_close_matches(key,data.keys())[0]]
        elif(yn=='N' or yn=='n'):
            return "The word doesn't exist,please double check\n"
        else:
            return "We don't understand the entry\n"
    else:
        return "The word doesn't exist\n"
def display(n):
    if (n==None):
        output = get(key)
    else:
        output = n
    if type(output)==list:
        for item in output:
            print(item)
    else:
        print(output)
display(None)
def checker():
    Nn=input("Do you wish to check another word-Y/N\n")
    if(Nn=='Y' or Nn=='y'):
        nkey=input("what you want to search?\n")
        n=get(nkey)
        display(n)
        checker()
    elif(Nn=='N' or Nn=='n'):
        time.sleep(1)
        print("Thanks for using our dictionary,\nWe would love to listen from you again")
    else:
        print("Sorry we didn't get that!")
        time.sleep(1)
        checker()
checker()
