class PaymentMethod:
    def __init__(self, name, card_number, expiration_date, cvv):
        self.name = name
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.cvv = cvv

    def process_payment(self, amount):
      
        print(f"Processing payment of ${amount:.2f} using {self.name} card ending in {self.card_number[-4:]}")
