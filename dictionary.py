import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def search(x):
    x=x.lower()
    if x in data:
        return data[x]
    elif x.title() in data:
        return data[x.title()]
    elif x.upper() in data:
        return data[x.upper()]
    elif len(get_close_matches(x, data.keys()))>0:
        print("Did you mean %s instead" %get_close_matches(x, data.keys())[0])
        decide=input("Press y for yes and n for no: ")
        if(decide == "y"):
            return data[get_close_matches(x, data.keys())[0]]
        elif(decide == "n"):
            return "Invalid word"
        else:
            print("Wrong choice.Please enter only y or n")
    else:
        print("Invalid word.Please enter correct word")

x=input("Enter the word you want to search : ")
output=search(x)

if type(output)==list:
    for item in output:
        print(item)
else:
 print(output)