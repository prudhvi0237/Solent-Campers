class Customer:
    def __init__(self):
        """
        Instantiates various customer objects.
        """
        self.small_van = 0
        self.medium_van = 0
        self.large_van = 0
        self.camping_sites = []
        self.rentalTime = 0

    def requestVan(self):
        """
        Takes a request from the customer for the number of vans.
        """

        small_van = input("How many small_van would you like to rent?")
        try:
            small_van = int(small_van)
        except ValueError:
            print("That's not a positive integer!")
            return -1

        if small_van < 0:
            print("Invalid input. Number of small_van shouldnot be negative!")
            return -1
        else:
            self.small_van = small_van

        medium_van = input("How many medium_van would you like to rent?")
        try:
            medium_van = int(medium_van)
        except ValueError:
            print("That's not a positive integer!")
            return -1

        if medium_van < 0:
            print("Invalid input. Number of medium_van should not be negative!")
            return -1
        else:
            self.medium_van = medium_van

        large_van = input("How many large_van would you like to rent?")
        try:
            large_van = int(large_van)
        except ValueError:
            print("That's not a positive integer!")
            return -1

        if large_van < 0:
            print("Invalid input. Number of large_van should not be negative!")
            return -1
        else:
            self.large_van = large_van

        return [self.small_van, self.medium_van, self.large_van]

    def returnVan(self):
        """
        Allows customers to return their small_van to the rental shop.
        """
        if self.rentalTime and self.small_van and self.medium_van and self.large_van:
            return self.rentalTime, self.small_van, self.medium_van, self.large_van
        else:
            return 0, 0, 0, 0

    def requestCamp(self):
        """
        Takes a request from the customer for booking camping site.
        """
        input_string = input(
            "Enter the camping site(s) you want to book(separated with spaces): "
        )
        if input_string:
            input_camp_list = input_string.split(" ")
            self.camping_sites = input_camp_list
        return self.camping_sites

    def cancelCamp(self):
        """
        Allows customers to cancel camping sites.
        """
        if self.camping_sites:
            return self.camping_sites
        else:
            return []
