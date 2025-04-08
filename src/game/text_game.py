import random
from game.solitaire import Solitaire

def game_test():
    test = Solitaire()
    test.create_deck()
    test.construct_puzzle()
    test.create_stock()

    while True:
        print("\nCommands:")
        print("1: Draw a card")
        print("2: Place a card")
        print("3: Show tableau")
        print("4: Move Card")
        print("5: Exit")
        if test.waste:
            print(f"Card in hand: {test.waste[-1]}")
        command = input("Enter command: ")

        if command == "1":
            if test.stock:
                test.draw_card()
            else: 
                test.stock = test.waste[:]
                test.waste = [] 
                random.shuffle(test.stock)
                test.draw_card() 

        elif command == "2":
            if not test.waste:
                print("no card in waste to place")
                continue

            card = test.waste[-1]
            try:
                stack_number = int(input("Enter tableau stack number (1-7) to place the card: "))
                if 1 <= stack_number <= (len(test.tableau)):
                    stack = test.tableau[stack_number - 1]

                    if test.check_valid(card, stack):
                        stack.append({
                "card": card,
                "face_up": True
            })
                        test.waste.pop()
                        print(f"Placed {card} on tableau {stack_number}.")
                    else:
                        print("invalid move")

                else:
                    print("invalid tableau number")
            
            except ValueError:
                print("Please enter a valid number.")


        elif command == "3":
            for idx, stack in enumerate(test.tableau):
                cards = ["??" if not info["face_up"] else info["card"] for info in stack]
                print(f"Tableau {idx + 1}: {cards}")

        elif command == "4":
            print("this will be for moving cards around")
        
        elif command == "5":
            print("you lost I guess")
            break

        else:
            print("invalid command")


if __name__ == "__main__":
    game_test()