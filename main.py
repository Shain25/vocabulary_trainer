from modes import edit_mode, training_mode, test_mode
def main_menu():     
    while True:
        menu=input("Welcome to Englearn! please choose mode:\n1.Editing Mode\n2.Training Mode\n3.Testing Mode\n4.Exit\nPlease type the number of your choice: ")
        if menu=='1':
            edit_mode()
        elif menu=='2':
            training_mode()
            print('2')
        elif menu=='3':
            test_mode()
        elif menu=='4':
            print("You chose to exit the app, see you next time!")
            break
        else:
            print("Option unavailable, please select 1-4")
main_menu()