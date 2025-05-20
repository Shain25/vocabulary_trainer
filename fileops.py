import json

json_file="vocab_hebrew.json"

def load_vocab():
    try:
        with open(json_file, "r", encoding="utf-8") as file:
            data=json.load(file)
            return data
        print("for test: loaded the file")
    except FileNotFoundError:
        print("File not found, creating new one")
        return {} 

def save_vocab(data):
    try:
        with open(json_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print("Vocabulary updated successfully")
    except IOError:
        print("Error, Can't write to file")
        return False