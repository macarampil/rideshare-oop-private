class PassengerAccount:
    def __init__(self, name,):
        self.name = name
        self.__wallet_balance = 0.0

    def top_up_wallet(self, amount):
        if amount < 0:
            raise ValueError("Top-up amount CANNOT be negative")
        self.__wallet_balance += amount

    def pay_for_ride(self, fare_amount):
        if fare_amount < 0:
            raise ValueError("Fare amount CANNOT be negative")
        if fare_amount > self.__wallet_balance:
            raise ValueError("Insufficient funds! Please top up.")
        self.__wallet_balance -= fare_amount
        print(f" Remaining balance: {self.__wallet_balance}")

p1 = PassengerAccount("Reign")
p1.top_up_wallet(-100)
p1.pay_for_ride(20)
