from fileops import load_vocab, save_vocab

def edit_mode():
        while True:
            edit_menu=input("Which edit do you want to make?\n1.Add new word\n2.Delete a word\n3.Modify a word or its meaning\n4.Show all words in a unit\n5.Back to main menu\n")
            if edit_menu=='1':
                word_choice=input("Please type the word you want to add ")
                meaning_choice=input("Please type the meaning of the word ")
                unit_choice=input("Please type the unit number you want to add the word to ")
                unit_choice="unit_"+str(unit_choice)
                data=load_vocab()
                if unit_choice in data:
                    data[unit_choice].append({"word":word_choice, "meaning":meaning_choice})
                save_vocab(data)
            elif edit_menu=='2':
                delete_word=input("Please type the word you want to delete ")
                unit_choice=input("Please type the unit number you want to delete the word from ")
                unit_choice="unit_"+str(unit_choice)
                data=load_vocab()
                data[unit_choice]=[entry for entry in data[unit_choice] if entry["word"]!=delete_word]
                save_vocab(data)
            elif edit_menu=='3':
                old_word=input("Please type the word you want to update ")               
                unit_choice=input("Please type the unit number of the word you want to update ")
                unit_choice="unit_"+str(unit_choice)                
                new_word=input("Please type the new word ")
                new_meaning=input("Please type its meaning ")
                data=load_vocab()
                data[unit_choice]=[entry for entry in data[unit_choice] if entry["word"]!=old_word]
                data[unit_choice].append({"word":new_word, "meaning":new_meaning})
                save_vocab(data)                
            elif edit_menu=='4':
                data=load_vocab()
                print(data)
            elif edit_menu=='5':
                print("You Chose to go back to main menu ")
                break
            else:
                print("Option unavailable, please select 1-5 ")

def training_mode():
    data=load_vocab()
    print("Training Units:")
    for unit in data.keys():
        print(unit)
    choose_unit=input("Please choose a unit number: ")
    choose_unit="unit_"+str(choose_unit)
    words=[item["word"] for item in data[choose_unit]]
    print("Words in the unit you chose: "+", ".join(words))
    print("Practice full unit or a range? ")
    full_or_range=input("1. Full unit\n2. Range\n")
    if full_or_range=='1':
        
    if full_or_range=='2':

def test_mode():
    print("")