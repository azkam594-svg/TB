import menu.product_menu as products
import menu.promotion_menu as promotions
import menu.transaction_menu as transactions
import menu.statistic_menu as statistics


from rich import print  #styling output with rich library

def main():  #Main menu untuk mengakses semua fitur aplikasi
    while True:
        print("[blue]==+==+== APPLICATION STORE MANAGEMENT ==+==+==[/blue]")
        print("[yellow]1. Manage Products[/yellow]")
        print("[yellow]2. Manage Promotions[/yellow]")
        print("[yellow]3. Manage Transactions[/yellow]")
        print("[yellow]4. Store Statistics[/yellow]")
        print("[yellow]0. Exit[/yellow]")
        choice = input("Select an option: ")

        if choice == '1':
            products.product_menu()
            
        elif choice == '2':
            promotions.promotion_menu()
            
        elif choice == '3':
            transactions.transaction_menu()
            
        elif choice == '4':
            statistics.statistic_menu()
            
        elif choice == '0':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
            
            
if __name__ == "__main__":
    main()  