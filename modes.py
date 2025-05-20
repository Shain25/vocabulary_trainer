from fileops import load_vocab, save_vocab
import random
import time

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
    meanings={item["word"]:item["meaning"] for item in data[choose_unit]}
    print("Words in the unit you chose: "+", ".join(words))
    print("Practice full unit or a range? ")
    full_or_range=input("1. Full unit\n2. Range\n")
    if full_or_range=='1':
        repeat_count=words*7
        random.shuffle(repeat_count)
        for word in repeat_count:
            print("The word is:\n"+word)
            time.sleep(3)
            print("Its meaning is:\n"+meanings[word][::-1])
            if word != repeat_count[-1]:
                input("press Enter to proceed")

    if full_or_range=='2':
        start_word=input("Type the first word in range ").lower()
        end_word=input("Type the last word in range ").lower()
        range_words=[]
        if start_word and end_word in words and words.index(start_word)<words.index(end_word):
            for i in range(words.index(start_word), words.index(end_word)+1):
                range_words.append(words[i])
            repeat_count=range_words*7
            random.shuffle(repeat_count)
            print(repeat_count)
            for word in repeat_count:
                print("The word is:\n"+word)
                time.sleep(3)
                print("Its meaning is:\n"+meanings[word][::-1])
                if word != repeat_count[-1]:
                    input("press Enter to proceed")
        else:
            print("Error, please type words in a reasonable range!")



def test_mode():
    data=load_vocab()
    print("Test Units:")
    for unit in data.keys():
        print(unit)
    choose_unit=input("Please choose a unit number for your test: ")
    choose_unit="unit_"+str(choose_unit)
    correct_num=0
    wrong_num=0
    wrong_words=[]
    qnum=1
    for i in data[choose_unit]:
        print(f"Question number {qnum}")
        qnum+=1
        print(i['word'])
        answer=input("What is the meaning? ")
        if answer==i['meaning']:
            correct_num+=1
        else:
            wrong_num+=1
            wrong_words.append(i['word'])
    print("The test is over! here is your score feedback:")
    print(f"Total questions: {qnum-1}")
    print(f"Correct answers: {correct_num}")
    print(f"Wrong answers: {wrong_num}: {', '.join(wrong_words)} ")
    score=int((correct_num/(qnum-1))*100)
    print(f"Your score: {score}")
    if score>=85:
        print("Excellent! Great job remembering your vocabulary")
    if score>=60 and score<85:
        print("Good work! A bit more practice and you'll master it")
    if score>=30 and score<60:
        print("Keep going! You're getting there, but review needed")
    if score<30:
        print("Needs improvement. Study the words again and try once more")
    input("Press ENTER to go back to main menu")