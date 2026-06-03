from database.data import transactions

from services.transaction_service import add_transaction, view_transactions, saldo_transaction, laporan_transaction, delete_transaction

from rich import print


def transaction_menu(): #Menu untuk manage transactions
    while True:
        print("[bold blue]=+= Transaction Menu =+=[/bold blue]")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. View Saldo")
        print("4. Delete Transaction")
        print("5. Generate Transaction Report")
        print("0. Back to Main Menu")
        
        choice = input("Select an options: ")

        if choice == "1":
            sku = input("Enter product SKU: ")
            quantity = int(input("Enter quantity: "))
            date = input("Enter transaction date (YYYY-MM-DD HH:MM:SS): ")
            add_transaction(sku, quantity, date)

        elif choice == "2":
            view_transactions()

        elif choice == "3": 
            saldo_transaction()
        elif choice == "4":
            delete_transaction()
        elif choice == "5":
            laporan_transaction()
        elif choice == "0":
            print("[green]Returning to Main Menu...[/green]")
            break
        else:
            print("[red]Invalid option. Please try again.[/red]")