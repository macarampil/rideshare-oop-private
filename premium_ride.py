from base_ride import Ride

class PremiumRide(Ride):
    def __init__(self, distance_km, snack):
        super().__init__(distance_km)
        self.__complimentary_snack = snack
        self.__premium_base_rate = 15.0

    def calculate_fare(self):
        return self.__premium_base_rate + (self.distance_km * 3.00)

    def start_ride(self):
        print("Starting Premium Ride. Enjoy your snack!")

    def complete_ride(self):
        print(f"=== VIP RECEIPT ===\nFare: Php {self.calculate_fare():.2f}")
        print(f"Complimentary Snack: {self.__complimentary_snack}")
