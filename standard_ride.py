from Ride import Ride

class StandardRide(Ride):

    def __init__(self, distance_km):
        super().__init__(distance_km)
        self.__base_rate = 5.00

    def calculate_fare(self):
        return self.__base_rate + (self.distance_km * 1.50)

    def start_ride(self):
        print(f"Starting Standard Ride for {self.distance_km} km.")

    def complete_ride(self):
        print("=== STANDARD RECEIPT ===")
        print(f"Fare: Php{self.calculate_fare():.2f}")
