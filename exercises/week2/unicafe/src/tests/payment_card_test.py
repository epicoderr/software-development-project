import unittest
from cash_register import CashRegister
from payment_card import PaymentCard

class TestPaymentCard(unittest.TestCase):
    def test_initial_state(self):
        register = CashRegister()
        self.assertEqual(register.money, 100000)
        self.assertEqual(register.cheap, 0)
        self.assertEqual(register.yummy, 0)

    def test_eat_cheap_with_cash_sufficient(self):
        register = CashRegister()
        change = register.eat_cheap_with_cash(300)
        self.assertEqual(change, 60)
        self.assertEqual(register.money, 100240)
        self.assertEqual(register.cheap, 1)

    def test_eat_cheap_with_cash_insufficient(self):
        register = CashRegister()
        change = register.eat_cheap_with_cash(200)
        self.assertEqual(change, 200)
        self.assertEqual(register.money, 100000)
        self.assertEqual(register.cheap, 0)

    def test_eat_yummy_with_cash_sufficient(self):
        register = CashRegister()
        change = register.eat_yummy_with_cash(500)
        self.assertEqual(change, 100)
        self.assertEqual(register.money, 100400)
        self.assertEqual(register.yummy, 1)

    def test_eat_yummy_with_cash_insufficient(self):
        register = CashRegister()
        change = register.eat_yummy_with_cash(300)
        self.assertEqual(change, 300)
        self.assertEqual(register.money, 100000)
        self.assertEqual(register.yummy, 0)

    def test_eat_cheap_with_card_sufficient(self):
        register = CashRegister()
        card = PaymentCard(300)
        result = register.eat_cheap_with_card(card)
        self.assertTrue(result)
        self.assertEqual(card.balance, 60)
        self.assertEqual(register.cheap, 1)
        self.assertEqual(register.money, 100000)

    def test_eat_cheap_with_card_insufficient(self):
        register = CashRegister()
        card = PaymentCard(200)
        result = register.eat_cheap_with_card(card)
        self.assertFalse(result)
        self.assertEqual(card.balance, 200)
        self.assertEqual(register.cheap, 0)
        self.assertEqual(register.money, 100000)

    def test_eat_yummy_with_card_sufficient(self):
        register = CashRegister()
        card = PaymentCard(500)
        result = register.eat_yummy_with_card(card)
        self.assertTrue(result)
        self.assertEqual(card.balance, 100)
        self.assertEqual(register.yummy, 1)
        self.assertEqual(register.money, 100000)

    def test_eat_yummy_with_card_insufficient(self):
        register = CashRegister()
        card = PaymentCard(300)
        result = register.eat_yummy_with_card(card)
        self.assertFalse(result)
        self.assertEqual(card.balance, 300)
        self.assertEqual(register.yummy, 0)
        self.assertEqual(register.money, 100000)

    def test_add_money_to_card(self):
        register = CashRegister()
        card = PaymentCard(0)
        register.add_money_to_card(card, 500)
        self.assertEqual(card.balance, 500)
        self.assertEqual(register.money, 100500)

    def test_take_money_from_card(self):
        register = CashRegister()
        card = PaymentCard(200)
        register.add_money_to_card(card, -100)
        self.assertEqual(card.balance, 200)
        self.assertEqual(register.money, 100000)

    def test_take_money_insufficient(self):
        card = PaymentCard(200)
        result = card.take_money(300)
        self.assertFalse(result)
        self.assertEqual(card.balance, 200)

    def test_balance_in_euros(self):
        card = PaymentCard(500)
        self.assertEqual(card.balance_in_euros(), 5.00)

    def test_str_representation(self):
        card = PaymentCard(9760)
        self.assertEqual(str(card), "The card has 97.60 euros on it")

    def test_money_in_euros(self):
        register = CashRegister()
        
        self.assertEqual(register.money_in_euros(), 1000.00)
        
        card = PaymentCard(0)
        register.add_money_to_card(card, 500)
        self.assertEqual(register.money_in_euros(), 1005.00)  
        
        register.eat_cheap_with_cash(300)
        self.assertEqual(register.money_in_euros(), 1005.00 + 2.40)  