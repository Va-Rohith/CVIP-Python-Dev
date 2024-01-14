from colorama import Fore

class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

class ExpenseSharingApp:
    def __init__(self) -> None:
        self.roommates = []

    def get_roommates(self) -> None:
        num = int(input(Fore.LIGHTMAGENTA_EX + "Enter number of roommates: " + Fore.RESET))
        for i in range(1, num + 1):
            self.roommates.append(input(f"Enter roommate - {i} Name: ").capitalize())

    @staticmethod
    def show_expenses(lst, amount) -> None:
        max_name_length = max(len(name) for name in lst)
        max_amount_length = len("Amount to be Paid")

        print(Fore.LIGHTYELLOW_EX + Color.UNDERLINE + "\nSplitted Amount Bill" + Color.END + Fore.RESET)
        
        print(f"\n\t {'Name':<{max_name_length}} \t\t {'Amount to be Paid':<{max_name_length}}")
        print("\t" + "-" * (max_name_length + max_amount_length + 20))
        for roommate in lst:
            print(f"\t {roommate:<{max_name_length}} \t\t ₹ {amount:<{max_name_length}}")

    def split_bills(self, total_amount) -> None:
        if total_amount <= 0:
            exit(Fore.RED + "Exited with code 0: Amount Can't be Negative" + Fore.RESET)

        amount_per_person = total_amount / len(self.roommates)
        amount_per_person = round(amount_per_person, 2)

        self.show_expenses(self.roommates, amount_per_person)

    @staticmethod
    def show_paid_and_not_paid(paid_list, roommates) -> None:
        max_name_length = max(len(name) for name in roommates)
        max_status_length = len("Paid/Not Paid")

        print(Fore.LIGHTYELLOW_EX + Color.UNDERLINE + "\nList of Paid and Not Paid Persons" + Color.END + Fore.RESET)

        print(f"\n\t {'Name':<{max_name_length}} \t\t {'Paid/Not Paid':{max_name_length}}")
        print("\t" + "-" * (max_name_length + max_status_length + 20))

        for name in roommates:
            status = "Paid" if name in paid_list else "Not Paid"
            print(f"\t {name:<{max_name_length}} \t\t {status:<{max_name_length}}")

    def track_payments(self) -> None:
        paid_list = []

        while True:
            paid_name = input(Fore.LIGHTMAGENTA_EX + "\nPress 0 to Exit or Enter your name if you paid: " + Fore.RESET).capitalize()

            if paid_name == '0':
                break

            # paid_name = input(Fore.LIGHTMAGENTA_EX + "\nEnter who have paid the amount: " + Fore.RESET).capitalize()

            if paid_name not in self.roommates:
                print(Fore.RED + "Invalid User Name!!!" + Fore.RESET)
            else:
                paid_list.append(paid_name)

            if sorted(self.roommates) == sorted(paid_list):
                break

        self.show_paid_and_not_paid(paid_list, self.roommates)


if __name__ == "__main__":
    print(Fore.BLUE + Color.BOLD + Color.UNDERLINE + "\n\t\t\t\t\t Expense Tracker App\n" + Color.END + Fore.RESET)

    app = ExpenseSharingApp()

    # Adding Users (Roommates in our case)
    app.get_roommates()

    # Adding and Splitting Bills among Roommates
    total_amount = float(input(Fore.LIGHTMAGENTA_EX + "\nEnter Total Bill Amount: " + Fore.RESET))
    app.split_bills(total_amount)

    # Tracking Paid & Not Paid Persons
    app.track_payments()
