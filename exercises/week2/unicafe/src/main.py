from payment_card import PaymentCard
from cash_register import Cashregister


def main():
    unicafe_exactum = Cashregister()
    kortti = PaymentCard(10000)

    unicafe_exactum.eat_cheap_with_card(kortti)

    print(unicafe_exactum.cheap)
    print(kortti)


if __name__ == "__main__":
    main()
