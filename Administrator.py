class Administrator:
    def __init__(self):
        """
        Instantiates various admin objects.
        """
        self.small_van = 0
        self.medium_van = 0
        self.large_van = 0
        self.camping_sites = []

    def addVan(self):
        """
        Add small/medium/large van(s) to the list of vans.
        """
        small_van = input("Enter the number of small vans to add :")
        try:
            small_van = int(small_van)
        except ValueError:
            print("That's not a positive integer!")
            return -1

        if small_van < 0:
            print("Invalid input. Number of small van shouldn't be negative!")
            return -1
        else:
            self.small_van = small_van

        medium_van = input("Enter the number of medium vans to add :")
        try:
            medium_van = int(medium_van)
        except ValueError:
            print("That's not a positive integer!")
            return -1

        if medium_van < 0:
            print("Invalid input. Number of medium van should not be negative!")
            return -1
        else:
            self.medium_van = medium_van

        large_van = input("Enter the number of large vans to add :")
        try:
            large_van = int(large_van)
        except ValueError:
            print("That's not a positive integer!")
            return -1

        if large_van < 0:
            print("Invalid input. Number of large van should not be negative!")
            return -1
        else:
            self.large_van = large_van

        return [self.small_van, self.medium_van, self.large_van]

    def removeVan(self):
        """
        Remove small/medium/large van(s) to the list of vans.
        """
        small_van = input("Enter the number of small vans to remove :")
        try:
            small_van = int(small_van)
        except ValueError:
            print("That's not a positive integer!")
            return -1

        if small_van < 0:
            print("Invalid input. Number of small van shouldnot be negative!")
            return -1
        else:
            self.small_van = small_van

        medium_van = input("Enter the number of medium vans to remove :")
        try:
            medium_van = int(medium_van)
        except ValueError:
            print("That's not a positive integer!")
            return -1

        if medium_van < 0:
            print("Invalid input. Number of medium van should not be negative!")
            return -1
        else:
            self.medium_van = medium_van

        large_van = input("Enter the number of large vans to remove :")
        try:
            large_van = int(large_van)
        except ValueError:
            print("That's not a positive integer!")
            return -1

        if large_van < 0:
            print("Invalid input. Number of large van should not be negative!")
            return -1
        else:
            self.large_van = large_van

        return [self.small_van, self.medium_van, self.large_van]

    def addCampingSite(self):
        """
        Add camping site(s) to the list of camping sites.
        """
        input_string = input(
            "Enter the camping site(s) you want to book(separated with spaces): "
        )
        if input_string:
            input_camp_list = input_string.split(" ")
            self.camping_sites = input_camp_list
        return self.camping_sites

    def removeCampingSite(self):
        """
        Remove camping site(s) to the list of camping sites.
        """
        input_string = input(
            "Enter the camping site(s) you want to remove(separated with spaces): "
        )
        if input_string:
            input_camp_list = input_string.split(" ")
            self.camping_sites = input_camp_list
        return self.camping_sites
