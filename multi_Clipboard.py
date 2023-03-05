# Allow to store multiple things on Clipboard

import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"

# create json file and save items
def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

def load_data(filepath, data):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}

# create argument
if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA, "")

    if command == "save":
        key = input("Enter a Key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Data saved!")
    elif command == "load":
        key = input("Enter a Key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard.")

        else:
            print("Key does not exist.")

    elif command == "list":
        print(data)
    else:
        print('Unknown command')    
else:
    print('please pass exactly one command.')