import Summary as su
import json
import csv


def advisor(van_obj, camp_obj, customer):
    while True:
        print(
            """
        ====== Advisor booking portal =======
        1. Display available vans
        2. Display available & booked camping sites
        3. Book van(s)
        4. Return van(s)
        5. Book camping site(s)
        6. Cancel booked camping site(s)
        7. Exit
        """
        )

        choice = input("Enter choice: ")

        try:
            choice = int(choice)
        except ValueError:
            print("That's not an int!")
            continue

        if choice == 1:
            van_obj.availableVan()
        elif choice == 2:
            camp_obj.availableCampSites()
        elif choice == 3:
            customer.rentalTime = van_obj.rentVan(customer.requestVan())
        elif choice == 4:
            van_obj.returnVan(customer.returnVan())
            (
                customer.rentalTime,
                customer.small_van,
                customer.medium_van,
                customer.large_van,
            ) = (0, 0, 0, 0)
        elif choice == 5:
            camp_obj.bookCampSites(customer.requestCamp())
        elif choice == 6:
            camp_obj.cancelCampSites(customer.cancelCamp())
            customer.camping_sites = []
        elif choice == 7:
            break
        else:
            print("Invalid input. Please enter number between 1-7")


def administrator(van_obj, camp_obj, admin):
    while True:
        print(
            """
        ====== Admin portal =======
        1. Add van(s)
        2. Add camping site(s)
        3. Remove van(s)
        4. Remove camping site(s)
        5. Exit
        """
        )

        choice = input("Enter choice: ")

        try:
            choice = int(choice)
        except ValueError:
            print("That's not an int!")
            continue

        def display():
            if choice == 1 or choice == 3:
                van_obj.availableVan()
            if choice == 2 or choice == 4:
                camp_obj.availableCampSites()

        display()
        if choice == 1:
            van_obj.addVanByAdmin(admin.addVan())
        elif choice == 2:
            camp_obj.addCampSites(admin.addCampingSite())
        elif choice == 3:
            van_obj.removeVanByAdmin(admin.removeVan())
            admin.small_van, admin.medium_van, admin.large_van = 0, 0, 0
        elif choice == 4:
            camp_obj.removeCampSites(admin.removeCampingSite())
            admin.camping_sites = []
        elif choice == 5:
            break
        else:
            print("Invalid input. Please enter number between 1-5")

        print("Updated data ==>")
        display()


def customer():
    while True:
        print(
            """
        1. See booking details
        2. Exit
        """
        )
        choice = input("Enter choice: ")
        try:
            choice = int(choice)
        except ValueError:
            print("That's not an int!")
            continue
        if choice == 1:
            if su.CUSTOMER_BOOKING:
                print("\n===Your booking details are===\n")
                print(json.dumps(su.CUSTOMER_BOOKING, indent=4, default=str))
                # data = json.loads(json.dumps(su.CUSTOMER_BOOKING))
                with open("booking_summary.csv", "w") as f:
                    w = csv.DictWriter(f, su.CUSTOMER_BOOKING.keys())
                    w.writeheader()
                    w.writerow(su.CUSTOMER_BOOKING)
        elif choice == 2:
            break
        else:
            print("Invalid input. Please select choice 1 or 2 ")
