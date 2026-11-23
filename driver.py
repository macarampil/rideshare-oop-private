class DriverAccount:
    def __init__(self, name, vehicle_plate):
        self.name = name
        self.vehicle_plate = vehicle_plate
        # TODO: Create private attributes for rating (starts at 5.0) and total_trips (starts at 0)
        self.__rating = 5.0
        self.__total_trips = 0

    def add_rating(self, new_rating):
        # TODO: If new rating is < 1.0 or > 5.0, raise ValueError ("Invalid rating!")
        if new_rating < 1.0 or new_rating > 5.0:
            raise ValueError("Invalid rating!")
        # TODO: Update the average rating and incremental total trips
        total_score = (self.__rating * self.__total_trips) + new_rating
        self.__total_trips += 1
        self.__rating = total_score / self.__total_trips

    def get_rating_info(self):
        # TODO: Return a string showing the driver's current average rating and total trips
        return f"Driver: {self.name}, Average Rating: {self.__rating:.2f}, Total Trips: {self.__total_trips}"


if __name__ == "__main__":
    driver = DriverAccount("John Doe", "ABC-1234")
    print(driver.get_rating_info())

    driver.add_rating(4.0)
    print(driver.get_rating_info())

    driver.add_rating(5.0)
    print(driver.get_rating_info())

    try:
        driver.add_rating(6.0)
    except ValueError as e:
        print(f"Caught expected error: {e}")

