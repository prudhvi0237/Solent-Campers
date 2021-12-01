import unittest
from datetime import datetime
from Van import Van
from Customer import Customer
from Campingsites import CampSite


class VanRentalTest(unittest.TestCase):
    def test_Van_Rental_diplays_correct_stock(self):
        print("\ntest_return_van_with_valid_input running..")
        van1 = Van()
        van2 = Van(10, 20, 25)
        self.assertEqual(van1.availableVan(), (10, 10, 10, 30))
        self.assertEqual(van2.availableVan(), (10, 20, 25, 55))

    def test_rentVan_for_negative_input(self):
        print("\ntest_rentVan_for_negative_input running..")
        van = Van()
        self.assertEqual(van.rentVan([-1, -2, -3]), None)

    def test_rentVan_for_zero_input(self):
        print("\ntest_rentVan_for_zero_input running..")
        van = Van()
        self.assertEqual(van.rentVan([0, 0, 0]), None)

    def test_rentVan_for_out_of_stock(self):
        print("\ntest_rentVan_for_out_of_stock running..")
        van = Van()
        self.assertEqual(van.rentVan([20, 35, 40]), None)

    def test_rentVan_for_valid_input(self):
        print("\ntest_rentVan_for_valid_input running..")
        van = Van()
        hour = datetime.now().hour
        self.assertEqual(van.rentVan([4, 3, 5]).hour, hour)

    def test_returnVan_valid_case(self):
        print("\ntest_returnVan_valid_case running..")
        van = Van()
        now = datetime.now()
        self.assertEqual(van.returnVan([now, 1, 2, 3]), None)

    def test_returnVan_invalid_case(self):
        print("\ntest_returnVan_invalid_case running..")
        van = Van()
        self.assertEqual(van.returnVan([0, 0, 0, 0]), None)

    def test_addVanByAdmin_valid_case(self):
        print("\ntest_addVanByAdmin_valid_case running..")
        van = Van()
        hour = datetime.now().hour
        self.assertEqual(van.addVanByAdmin([2, 1, 3]).hour, hour)

    def test_addVanByAdmin_invalid_case(self):
        print("\ntest_addVanByAdmin_invalid_case running..")
        van = Van()
        self.assertEqual(van.addVanByAdmin([0, 0, 0]), None)

    def test_removeVanByAdmin_invalid_case(self):
        print("\ntest_removeVanByAdmin_invalid_case running..")
        van = Van()
        self.assertEqual(van.removeVanByAdmin([0, 0, 0]), None)

    def test_removeVanByAdmin_out_of_boundary(self):
        print("\ntest_removeVanByAdmin_out_of_boundary running..")
        van = Van()
        self.assertEqual(van.removeVanByAdmin([15, 12, 13]), None)

    def test_removeVanByAdmin_valid_case(self):
        print("\ntest_removeVanByAdmin_valid_case running..")
        van = Van()
        hour = datetime.now().hour
        self.assertEqual(van.addVanByAdmin([2, 1, 3]).hour, hour)


class CampBookingTest(unittest.TestCase):
    def test_available_camping_sites(self):
        print("\ntest_available_camping_sites running..")
        camp1 = CampSite()
        camp2 = CampSite(["Bristol"])
        self.assertEqual(
            camp1.availableCampSites(), ["London", "Oxford", "Glasgow", "Manchester"]
        )
        self.assertEqual(camp2.availableCampSites(), ["Bristol"])

    def test_bookCampSites_with_zero_camps(self):
        print("\ntest_bookCampSites_with_zero_camps running..")
        camp1 = CampSite()
        self.assertEqual(camp1.bookCampSites([]), None)

    def test_bookCampSites_with_invalid_camps(self):
        print("\ntest_bookCampSites_with_invalid_camps running..")
        camp1 = CampSite()
        self.assertEqual(camp1.bookCampSites(["New"]), None)

    def test_bookCampSites_with_booked_camps(self):
        print("\ntest_bookCampSites_with_booked_camps running..")
        camp1 = CampSite()
        self.assertEqual(camp1.bookCampSites(["London", "Oxford"]), None)
        self.assertEqual(camp1.bookCampSites(["London"]), None)

    def test_bookCampSites_with_valid_camps(self):
        print("\ntest_bookCampSites_with_valid_camps running..")
        camp1 = CampSite()
        self.assertEqual(camp1.bookCampSites(["London", "Oxford", "Glasgow"]), None)

    def test_cancelCampSites_with_booking(self):
        print("\ntest_cancelCampSites_with_booking running..")
        camp1 = CampSite()
        self.assertEqual(camp1.cancelCampSites(["London"]), None)

    def test_cancelCampSites_without_booking(self):
        print("\ntest_cancelCampSites_without_booking running..")
        camp1 = CampSite()
        self.assertEqual(camp1.cancelCampSites([]), None)

    def test_addCampSites_invalid_case(self):
        print("\ntest_addCampSites_invalid_case running..")
        camp1 = CampSite()
        self.assertEqual(camp1.addCampSites([]), None)

    def test_addCampSites_already_present_camp(self):
        print("\ntest_addCampSites_already_present_camp running..")
        camp1 = CampSite()
        self.assertEqual(camp1.addCampSites(["London"]), None)

    def test_add_remove_CampSites_valid_camp(self):
        print("\ntest_add_remove_CampSites_valid_camp running..")
        camp3 = CampSite()
        self.assertEqual(camp3.addCampSites(["Liverpool"]), None)
        self.assertEqual(camp3.removeCampSites(["Liverpool"]), None)

    def test_remove_invalid_CampSites(self):
        print("\ntest_remove_invalid_CampSites running..")
        camp1 = CampSite()
        self.assertEqual(camp1.removeCampSites(["Leeds"]), None)

    def test_remove_booked_CampSites(self):
        print("\ntest_remove_booked_CampSites running..")
        camp1 = CampSite()
        self.assertEqual(camp1.bookCampSites(["Glasgow"]), None)
        self.assertEqual(camp1.removeCampSites(["Glasgow"]), None)


class CustomerTest(unittest.TestCase):
    def test_return_van_with_valid_input(self):
        print("\ntest_return_van_with_valid_input running..")
        # create a customer
        customer = Customer()

        # create valid customer attributes
        now = datetime.now()
        customer.rentalTime = now
        customer.small_van = 2
        customer.medium_van = 1
        customer.large_van = 3
        self.assertEqual(customer.returnVan(), (now, 2, 1, 3))

    def test_return_van_with_invalid_input(self):
        print("\ntest_return_van_with_invalid_input running..")
        # create a customer
        customer = Customer()

        # create invalid customer rentalTime
        now = datetime.now()
        customer.rentalTime = 0
        customer.small_van = 2
        customer.medium_van = 1
        customer.large_van = 3
        self.assertEqual(customer.returnVan(), (0, 0, 0, 0))

    def test_cancel_camping_sites_with_camps(self):
        print("\ntest_cancel_camping_sites_with_camps running..")
        # create a customer
        customer = Customer()

        # create valid customer attributes
        customer.camping_sites = ["London"]
        self.assertEqual(customer.cancelCamp(), ["London"])

    def test_cancel_camping_sites_without_camps(self):
        print("\ntest_cancel_camping_sites_without_camps running..")
        # create a customer
        customer = Customer()

        # create customer camping_sites as []
        customer.camping_sites = []
        self.assertEqual(customer.cancelCamp(), [])


if __name__ == "__main__":
    unittest.main()
