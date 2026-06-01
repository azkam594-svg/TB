from database.data import promotions, products

from services.promotion_service import add_promotion, view_promotions, update_promotion, delete_promotion, search_promotions

from rich import print #styling output with rich library


def promotion_menu():  #Menu untuk manage promotions
    while True:
        print("[bold blue]=+= Promotion Menu =+=[/bold blue]")
        print("1. Add Promotions")
        print("2. View Promotions")
        print("3. Update Promotions")
        print("4. Delete Promotions")
        print("5. Search Promotions")
        print("0. Back to Main Menu")
        
        choice = input("Select an options: ")

        if choice == "1":
            sku = input("Enter product SKU: ")
            
            # Cek apakah SKU ada di database products
            if not any(product["sku"] == sku for product in products):
                print("[red]SKU tidak ditemukan di database produk.[/red]")
            # Cek apakah SKU sudah ada di promosi
            elif any(promo["sku"] == sku for promo in promotions):
                print("[red]SKU promosi sudah digunakan.[/red]")
            else:
                diskon = int(input("Enter discount percentage: "))
                add_promotion(sku, diskon)

        elif choice == "2":
            view_promotions()

        elif choice == "3": 
            update_promotion()
        
        elif choice == "4":
            delete_promotion()
        
        elif choice == "5":
            search_promotions()
        
        elif choice == "0":
            print("[green]Returning to Main Menu...[/green]")
            break
        
        else:
            print("[red]Invalid option. Please try again.[/red]")

