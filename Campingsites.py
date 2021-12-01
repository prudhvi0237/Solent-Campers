import datetime
import Summary as su


class CampSite:
    def __init__(
        self, camp_sites_available=["London", "Oxford", "Glasgow", "Manchester"]
    ):
        """
        Instantiates camping sites.
        Default camping sites - 'London','Oxford','Glasgow','Manchester'.
        """
        self.camp_sites_available = camp_sites_available
        self.camp_sites_booked = []

    def availableCampSites(self):
        """
        Displays the camping sites currently available to book.
        """
        print("Available camping sites to book: {}".format(self.camp_sites_available))
        if self.camp_sites_booked:
            print(
                "Booking unvailable for camping sites: {}".format(
                    self.camp_sites_booked
                )
            )
        return self.camp_sites_available

    def bookCampSites(self, camping_sites):
        """
        Function to book available camping sites to a customer.
        """
        if not camping_sites:
            print("You didn't enter any camping site!")
            return None
        else:
            invalid_camps = []
            booked_camps = []
            for camp in camping_sites:
                if camp not in self.camp_sites_available:
                    if camp in self.camp_sites_booked:
                        booked_camps.append(camp)
                    else:
                        invalid_camps.append(camp)
            if booked_camps:
                print(
                    "Your booking list contains camping site(s) {} which is/are already booked. Please retry!".format(
                        booked_camps
                    )
                )
                return None
            elif invalid_camps:
                print(
                    "Your booking list contains camping site(s) {} which is/are invalid. Please retry!".format(
                        invalid_camps
                    )
                )
                return None
            else:
                now = datetime.datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                print(
                    "You have booked {} camping site(s) on {}".format(
                        camping_sites, dt_string
                    )
                )
                print("We hope that you enjoy our service.")
                for camp in camping_sites:
                    self.camp_sites_available.remove(camp)
                    self.camp_sites_booked.append(camp)
                    su.CUSTOMER_BOOKING["camping_details"]["camp_sites"].append(camp)
                su.CUSTOMER_BOOKING["camping_details"]["camp_booking_time"] = dt_string
                return None

    def cancelCampSites(self, camping_sites):
        """
        Cancels the list of booked camping sites
        """
        if camping_sites:
            self.camp_sites_available = [*self.camp_sites_available,*self.camp_sites_booked]
            self.camp_sites_booked = su.CUSTOMER_BOOKING["camping_details"][
                "camp_sites"
            ] = []
            su.CUSTOMER_BOOKING["camping_details"]["camp_booking_time"] = None
            print("Your cancellation is confirmed. Please visit us again !")
            return None
        else:
            print("Are you sure you booked camping site with us?")
            return None

    def addCampSites(self, camping_sites):
        """
        Adds camping sites to list of camping sites
        """
        if not camping_sites:
            print("You didn't enter any camping site!")
            return None
        else:
            current_camps = [*self.camp_sites_available, *self.camp_sites_booked]
            added_camps = []
            unadded_camps = []
            for camp in camping_sites:
                if camp not in current_camps:
                    self.camp_sites_available.append(camp)
                    added_camps.append(camp)
                else:
                    unadded_camps.append(camp)
            if added_camps:
                print("Your have added camping site(s) - {}".format(added_camps))
            if unadded_camps:
                print(
                    "The camping sites {} are already present in database".format(
                        unadded_camps
                    )
                )
            return None

    def removeCampSites(self, camping_sites):
        """
        Removes camping sites from the list of camping sites.
        """
        if not camping_sites:
            print("You didn't enter any camping site!")
            return None
        else:
            available_camps = self.camp_sites_available
            booked_camps = self.camp_sites_booked
            removed_camps = []
            unremoved_camps = []
            for camp in camping_sites:
                if camp in available_camps:
                    self.camp_sites_available.remove(camp)
                    removed_camps.append(camp)
                elif camp in booked_camps:
                    unremoved_camps.append(camp)
                else:
                    print("Camping site '{}' not present to remove".format(camp))
            if removed_camps:
                print("Your have removed camping site(s) - {}".format(removed_camps))
            if unremoved_camps:
                print(
                    "The camping sites {} are booked, you cannot remove it now!".format(
                        unremoved_camps
                    )
                )
            return None
