class Battery(object):
    """
    A simple attempt to model a battery for an electric car.
    """

    def __init__(self, battery_size=75):
        """
        Initialize the battery's attributes.
        """
        self.battery_size = battery_size

    def describe_battery(
        self,
    ):
        """
        Print a statement describing the battery size.
        """
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(
        self,
    ):
        """
        Print a statement about the range this battery provides.
        """
        if self.battery_size == 75:
            miles_range = 260
        elif self.battery_size == 100:
            miles_range = 315
        else:
            # Provide a default range or handle other sizes
            miles_range = self.battery_size * 3.5

        print(f"This car can go about {miles_range} miles on a full charge.")