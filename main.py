from Van import Van
import RequestHandler as req
from Customer import Customer
from Administrator import Administrator
from Campingsites import CampSite


def main():
    van_obj = Van()
    camp_obj = CampSite()
    customer = Customer()
    admin = Administrator()

    print("\n###Welcome to Solent Campers###\n")
    while True:
        print("Enter the type of account you want to login -",end = "")
        print("""
        1. Customer
        2. Shop Advisor
        3. Administrator
        4. Exit from Solent Campers
        """)
        try:
            account_type = int(input("Enter choice: "))    
        except ValueError:
            print("That's not an integer! Give the correct integer value!")
            continue

        if account_type == 1:
            req.customer()
        elif account_type == 2:
            req.advisor(van_obj,camp_obj,customer)
        elif account_type == 3:
            req.administrator(van_obj,camp_obj,admin)
        elif account_type == 4:
            break
        else:
            print("Invalid input. Please enter the correct account type.")   

        print("Thank you for using the Solent Campers! Please visit again :)")


if __name__=="__main__":
    main()