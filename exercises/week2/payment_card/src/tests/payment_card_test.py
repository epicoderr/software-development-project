import unittest
from payment_card import PaymentCard

class TestPaymentCard(unittest.TestCase):
    def setUp(self):
        self.card = PaymentCard(1000)  

    def test_constructor_sets_the_balance_right(self):
        self.assertEqual(str(self.card), "The card has 10.00 euros on it")

    def test_eat_cheap_reduces_balance_right(self):
        self.card.eat_cheap()
        self.assertEqual(self.card.balance_in_euros(), 7.5)

    def test_eat_yummy_reduces_balance_right(self):
        self.card.eat_yummy()
        self.assertEqual(self.card.balance_in_euros(), 6.0)

    def test_eat_cheap_doesnt_make_balance_negative(self):
        card = PaymentCard(200)
        card.eat_cheap()
        self.assertEqual(card.balance_in_euros(), 2.0)

    def test_able_to_add_money(self):
        self.card.add_money(2500) 
        self.assertEqual(self.card.balance_in_euros(), 35.0)

    def test_balance_does_not_exceed_maximum(self):
        self.card.add_money(20000)  
        self.assertEqual(self.card.balance_in_euros(), 150.0)

    def test_eat_yummy_doesnt_make_balance_negative(self):
        card = PaymentCard(300) 
        card.eat_yummy()
        self.assertEqual(card.balance_in_euros(), 3.0)

    def test_adding_negative_money_does_nothing(self):
        self.card.add_money(-500)  
        self.assertEqual(self.card.balance_in_euros(), 10.0)

    def test_can_eat_cheap_with_exact_balance(self):
        card = PaymentCard(250) 
        card.eat_cheap()
        self.assertEqual(card.balance_in_euros(), 0.0)

    def test_can_eat_expensive_with_exact_balance(self):
        card = PaymentCard(400) 
        card.eat_yummy()
        self.assertEqual(card.balance_in_euros(), 0.0)

    def test_initial_balance(self):
        self.assertEqual(self.card.balance_in_euros(), 10.0)

    def test_adding_money_increases_balance(self):
        self.card.add_money(500)  
        self.assertEqual(self.card.balance_in_euros(), 15.0)

    def test_taking_money_decreases_balance_if_enough(self):
        result = self.card.spend_money(500)  
        self.assertTrue(result) 
        self.assertEqual(self.card.balance_in_euros(), 5.0)  

    def test_taking_money_doesnt_change_balance_if_not_enough(self):
        result = self.card.spend_money(2000)  
        self.assertFalse(result)  
        self.assertEqual(self.card.balance_in_euros(), 10.0) 