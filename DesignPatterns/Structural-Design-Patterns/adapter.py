from abc import ABC, abstractmethod
from datetime import datetime

class Payment(ABC):
    @abstractmethod
    def pay(self, amount:float, currency:str) -> str:
        '''Return transaction id'''

class Stripe:
    def make_payment(self, amount:float, currency:str) -> dict:
        return {"id": f"txn_id_{datetime.now()}", "amount": amount, "currency": currency}

class Paypal:
    def send_payment(self, amount: float) -> dict:
        return {"id": f"txn_id_{datetime.now()}", "status": "PASSED"}

class StripeAdapter(Payment):
    def __init__(self, sdk:Stripe) -> None:
        self._sdk = sdk

    def pay(self, amount: float, currency: str) -> str:
        transaction = self._sdk.make_payment(amount=amount, currency=currency)
        return transaction['id']

class PaypalAdapter(Payment):
    def __init__(self, sdk:Paypal) -> None:
        self._sdk = sdk

    def pay(self, amount: float, currency: str):
        transaction = self._sdk.send_payment(amount)
        return transaction['id']

def checkout(processor: Payment, amount_cents: float) -> None:
    txn_id = processor.pay(amount_cents, "USD")
    print(f"Paid. Transaction: {txn_id}")

if __name__ == "__main__":
    checkout(StripeAdapter(Stripe()), 1234)
    checkout(PaypalAdapter(Paypal()), 4567)
