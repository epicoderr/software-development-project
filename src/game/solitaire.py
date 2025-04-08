import random

class Solitaire:
    def __init__(self):
        self.deck = []  
        self.tableau = [[], [], [], [], [], [], []]
        self.foundations = [[], [], [], []] 
        self.stock = []  
        self.waste = [] 
        self.order = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def create_deck(self):
        suits = "CDHS"
        ranks = self.order
        
        self.deck = [f"{rank}{suit}" for suit in suits for rank in ranks]  
        random.shuffle(self.deck)  

        print(self.deck)
    
    def construct_puzzle(self):
        for i in range(7):
            for j in range(i+1):
                card = self.deck.pop()
                self.tableau[i].append({
                "card": card,
                "face_up": False
            })
            self.tableau[i][-1]["face_up"] = True

        print(self.tableau)
    
    def create_stock(self):
        random.shuffle(self.deck)  
        self.stock = self.deck[:]  

    def draw_card(self):
        self.waste.append(self.stock.pop())

    def place_card(self, card, stack):
        if self.check_valid(card, stack):
            stack.append(card)

    def check_valid(self, card, stack):
        if not stack:
            return True
        top = stack[-1]["card"]
        if card[-1] == top[-1]:
            if self.order.index(card[:-1]) == self.order.index(top[:-1]) -1:
                return True
        else:
            return False