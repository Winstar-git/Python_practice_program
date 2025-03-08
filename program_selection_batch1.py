# Create a funtion menu for program selection
def menu():
    def selection(prompt): # Create a funtion that limit the selection 
        while True:
            try:
                value = int(input(prompt))
                if 0 <= value <= 10:
                    return value
                else:
                    print('Invalid input. Please select a number in the choices.')
            except ValueError:
                print("Invalid input. Please enter valid number.")
# Create a the selection menu
    while True:
        print()
        print("Practice Program")
        print()
        print("[1] Prog01", "\t[6]  Prog06".expandtabs(tabsize=6))
        print("[2] Prog02", "\t[7]  Prog07".expandtabs(tabsize=6))
        print("[3] Prog03", "\t[8]  Prog08".expandtabs(tabsize=6))
        print("[4] Prog04", "\t[9]  Prog09".expandtabs(tabsize=6))
        print("[5] Prog05", "\t[10] Prog10".expandtabs(tabsize=6))
        print()
        print("[0]: Exit")
        print()
        choice = selection("Select an option: ")
        print()