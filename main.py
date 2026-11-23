from base_ride import Ride
from driver import DriverAccount
from passenger import PassengerAccount

if __name__ == "__main__":
    # Test PassengerAccount
    p1 = PassengerAccount("Reign")
    p1.top_up_wallet(100)
    p1.pay_for_ride(20)

    # Test DriverAccount
    driver = DriverAccount("John Doe", "ABC-1234")
    print(driver.get_rating_info())
    driver.add_rating(4.0)
    driver.add_rating(5.0)
    print(driver.get_rating_info())

