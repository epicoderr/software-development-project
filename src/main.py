import tkinter as tk
from tkinter import Tk, Toplevel, Label, Button, scrolledtext
from ui.ui import UI
from game.solitaire import Solitaire
import random

class SolitaireCLI(tk.Frame):
    def __init__(self, master, game):
        super().__init__(master)
        self.master = master
        self.game = game

        self.pack(expand=True, fill="both")

        #AI code
        self.output_text = scrolledtext.ScrolledText(self, wrap="word", height=20, width=50, state="disabled")
        self.output_text.pack(padx=10, pady=10, expand=True, fill="both")

        self.input_entry = tk.Entry(self)
        self.input_entry.pack(pady=5, fill="x")
        self.input_entry.bind("<Return>", self.process_command)

        self.initialize_game()
        #AI code end

    def initialize_game(self):
        """Initialize the Solitaire game logic."""
        self.game.create_deck()
        self.game.construct_puzzle()
        self.game.create_stock()
        self.display_output("Welcome to Solitaire CLI!\nEnter a command below:\n1: Draw a card\n2: Place a card\n3: Show tableau\n4: Move To Foundation\n5: Show foundation\n6: Exit")

    def display_output(self, text):
        """Display output in the text widget."""
        #AI code
        self.output_text.config(state="normal")
        self.output_text.insert("end", text + "\n")
        self.output_text.config(state="disabled")
        self.output_text.yview("end")  
        #AI code end

    def process_command(self, event):
        """Process the user command from the entry widget."""
        command = self.input_entry.get().strip()
        self.input_entry.delete(0, "end")

        if not command:
            return

        self.display_output(f"> {command}")

        if command == "1":
            if self.game.stock:
                self.game.draw_card()
                if self.game.waste:
                    self.display_output(f"Card drawn: {self.game.waste[-1]}")
            else:
                self.game.stock = self.game.waste[:]
                self.game.waste = []
                random.shuffle(self.game.stock)
                self.game.draw_card()
                self.display_output("Stock reset and shuffled.")

        elif command.startswith("2"):
            parts = command.split()
            if len(parts) != 2:
                self.display_output("Usage: 2 <tableau number>")
                return
            stack_number_str = parts[1]
            try:
                stack_number = int(stack_number_str)
            except ValueError:
                self.display_output("Please enter a valid number.")
                return

            if not self.game.waste:
                self.display_output("No card in waste to place.")
                return

            card = self.game.waste[-1]
            if 1 <= stack_number <= len(self.game.tableau):
                stack = self.game.tableau[stack_number - 1]

                if self.game.check_valid(card, stack):
                    stack.append({"card": card, "face_up": True})
                    self.game.waste.pop()
                    self.display_output(f"Placed {card} on tableau {stack_number}.")
                else:
                    self.display_output("Invalid move.")
            else:
                self.display_output("Invalid tableau number.")

        elif command == "3":
            for idx, stack in enumerate(self.game.tableau):
                cards = ["??" if not info["face_up"] else info["card"] for info in stack]
                self.display_output(f"Tableau {idx + 1}: {cards}")

        elif command.startswith("4"):
            parts = command.split()
            if len(parts) != 2:
                self.display_output("Usage: 4 <tableau number>")
                return
            stack_number_str = parts[1]
            try:
                stack_number = int(stack_number_str)
            except ValueError:
                self.display_output("Please enter a valid number.")
                return


        elif command == "5":
            self.display_output("This will show the state of the foundation")

        elif command == "6":
            self.display_output("Game Over. You lost, I guess!")
            self.master.quit()

        else:
            self.display_output("Invalid command.")

def start_game(start_screen, window):
    start_screen.destroy()

    window.deiconify()
    
    game = Solitaire()
    cli_view = SolitaireCLI(window, game)
    cli_view.pack(expand=True, fill="both")
    
    #ui_view = UI(window, game)
    #ui_view.start()

def main():
    window = tk.Tk()
    window.title("Solitaire")
    window.withdraw()
    
    start_screen = Toplevel(window)
    start_screen.title("Welcome to Solitaire")
    Label(start_screen, text="Welcome to Solitaire!").pack(padx=20, pady=20)
    Button(start_screen, text="Start Game", command=lambda: start_game(start_screen, window)).pack(pady=10)
    
    window.mainloop()

if __name__ == "__main__":
    main()