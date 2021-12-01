import datetime
import Summary as su


class Van:
    def __init__(self, small_van=10, medium_van=10, large_van=10):
        """
        Instantiates different types of vans.
        Default vans available in the beginning -
        small van : 10,medium van : 10,large van : 10
        """
        self.small_van = small_van
        self.medium_van = medium_van
        self.large_van = large_van

    def availableVan(self):
        """
        Displays the vans currently available for rent in the shop.
        """
        print(
            "Available vans to rent: {} small vans,{} medium vans and {} large vans".format(
                self.small_van, self.medium_van, self.large_van
            )
        )
        total_vans = self.small_van + self.medium_van + self.large_van
        print("Total vans available ==> ", total_vans)
        return self.small_van, self.medium_van, self.large_van, total_vans

    def rentVan(self, request):
        """
        Rents van to a customer.
        """
        small_van, medium_van, large_van = request
        if small_van < 0 or medium_van < 0 or large_van < 0:
            print("Number of vans should be positive!")
            return None
        elif small_van == 0 and medium_van == 0 and large_van == 0:
            print("Select atleast one of the 3 types of van(as positive number)!")
            return None
        elif (
            small_van > self.small_van
            or medium_van > self.medium_van
            or large_van > self.large_van
        ):
            print(
                "Sorry! We have currently {} small vans,{} medium vans and {} large vans available to rent..".format(
                    self.small_van, self.medium_van, self.large_van
                )
            )
            print("Please give the vans within range incase you retry to book")
            return None
        else:
            now = datetime.datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            print(
                "You have rented {} small vans,{} medium vans and {} large vans on {}".format(
                    small_van, medium_van, large_van, dt_string
                )
            )
            print("We hope that you enjoy our service.")
            if small_van > 0:
                self.small_van -= small_van
                su.CUSTOMER_BOOKING["van_details"]["small_van"] += small_van
                print(su.CUSTOMER_BOOKING["van_details"]["small_van"])
            if medium_van > 0:
                self.medium_van -= medium_van
                su.CUSTOMER_BOOKING["van_details"]["medium_van"] += medium_van
            if large_van > 0:
                self.large_van -= large_van
                su.CUSTOMER_BOOKING["van_details"]["large_van"] += large_van
            su.CUSTOMER_BOOKING["van_details"]["booking_time"] = dt_string
            return now

    def returnVan(self, request):
        """
        1. Accept a rented van from a customer
        2. Replensihes the inventory
        """
        rentalTime, small_van, medium_van, large_van = request
        if small_van >= 0 and medium_van >= 0 and large_van >= 0 and rentalTime:
            self.small_van += small_van
            self.medium_van += medium_van
            self.large_van += large_van
            now = datetime.datetime.now()
            rentalPeriod = now - rentalTime
            su.CUSTOMER_BOOKING["van_details"]["small_van"] = su.CUSTOMER_BOOKING[
                "van_details"
            ]["medium_van"] = su.CUSTOMER_BOOKING["van_details"]["large_van"] = 0
            su.CUSTOMER_BOOKING["van_details"]["booking_time"] = None
            print(
                "Thanks for returning your van. Hope you enjoyed our service for the duration {}!".format(
                    rentalPeriod
                )
            )
            return None
        else:
            print("Are you sure you rented a van with us?")
            return None

    def addVanByAdmin(self, request):
        """
        Adds van given by admin to the total vans
        """
        small_van, medium_van, large_van = request
        if small_van == 0 and medium_van == 0 and large_van == 0:
            print("You didn't add any vans!")
            return None
        else:
            now = datetime.datetime.now()
            print(
                "You have added {} small vans,{} medium vans and {} large vans on {}".format(
                    small_van, medium_van, large_van, now
                )
            )
            print("Thanks for your great work.")
            if small_van > 0:
                self.small_van += small_van
            if medium_van > 0:
                self.medium_van += medium_van
            if large_van > 0:
                self.large_van += large_van
            return now

    def removeVanByAdmin(self, request):
        """
        Removes van given by admin from the total vans
        """
        small_van, medium_van, large_van = request
        if small_van == 0 and medium_van == 0 and large_van == 0:
            print("You didn't remove any vans!")
            return None
        elif (
            small_van > self.small_van
            or medium_van > self.medium_van
            or large_van > self.large_van
        ):
            print(
                "Sorry! We have currently {} small vans,{} medium vans and {} large vans available to remove..".format(
                    self.small_van, self.medium_van, self.large_van
                )
            )
            print("Please give the vans within range incase you retry to remove")
            return None
        else:
            now = datetime.datetime.now()
            print(
                "You have removed {} small vans,{} medium vans and {} large vans on {}".format(
                    small_van, medium_van, large_van, now
                )
            )
            print("Thanks for your great work.")
            if small_van > 0:
                self.small_van -= small_van
            if medium_van > 0:
                self.medium_van -= medium_van
            if large_van > 0:
                self.large_van -= large_van
            return now
