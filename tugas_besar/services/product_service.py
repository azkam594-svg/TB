from database.data import products #Mengimpor daftar produk dari file data.py

# Import Rich library untuk mempercantik tampilan output di terminal
from rich.table import Table

from rich.console import Console

from rich import print


def add_product(product_name, sku, price, stock): #Menambahkan produk baru ke dalam daftar produk
    for product in products:
        if product["sku"] == sku:
            print("[red]SKU sudah digunakan, silakan gunakan SKU lain.[/red]")
            return
        
    product = {
        "product_name": product_name,
        "sku": sku,
        "price": price,
        "stock": stock
    }
    products.append(product)
    print(f"[green]{product_name} berhasil ditambahkan.[/green]")
    

def view_products(): #Menampilkan semua produk yang tersedia
    if not products:
        print("[yellow]Tidak ada produk yang tersedia.[/yellow]")
        return
    else:
        table = Table(title="Available Products")
        table.add_column("Product Name", style="blue")
        table.add_column("SKU", style="magenta")
        table.add_column("Price", style="green")
        table.add_column("Stock", style="yellow")

        for product in products:
            table.add_row(product["product_name"], product["sku"], str(product["price"]), str(product["stock"]))

        console = Console()
        console.print(table)


def search_products(): #Mencari produk berdasarkan nama atau SKU
    keyword = input("Enter product name or SKU to search: ")
    found_products = [product for product in products if keyword.lower() in product["product_name"].lower() or keyword.lower() in product["sku"].lower()]
    
    if found_products:
        for product in found_products:
            print(f"|Product Name: {product['product_name']}, |SKU: {product['sku']}, |Price: {product['price']}, |Stock: {product['stock']}|")
    else:
        print("[red]No products found matching the keyword.[/red]")


def update_product(): #Memperbarui informasi produk berdasarkan SKU
    sku = input("Enter SKU of the product to update: ")

    for product in products:
        if product["sku"] == sku:
            print("[blue]\nWhat do you want to update?")
            print("1. Product Name")
            print("2. Price")
            print("3. Stock")
            print("4. Update All")

            choice = input("Select an option: ")

            if choice == "1":
                new_name = input("Enter new product name: ")
                product["product_name"] = new_name

            elif choice == "2":
                new_price = input("Enter new price: ")
                product["price"] = float(new_price)

            elif choice == "3":
                new_stock = input("Enter new stock: ")
                product["stock"] = int(new_stock)

            elif choice == "4":
                new_name = input("Enter new product name (leave blank to keep current): ")
                new_price = input("Enter new price (leave blank to keep current): ")
                new_stock = input("Enter new stock (leave blank to keep current): ")

                if new_name:
                    product["product_name"] = new_name

                if new_price:
                    product["price"] = float(new_price)

                if new_stock:
                    product["stock"] = int(new_stock)

            else:
                print("[red]Invalid option. Please try again.")
                return

            print(f"[green]Product with SKU {sku} has been updated.[/green]")
            return

    print(f"[red]No product found with SKU {sku}.[/red]")


def delete_product(): #Menghapus produk dari daftar berdasarkan SKU
    sku = input("Enter SKU of the product to delete: ")
    for product in products:
        if product["sku"] == sku:
            products.remove(product)
            print(f"[green]Product with SKU {sku} has been deleted.[/green]")
            return
    
    print(f"[red]No product found with SKU {sku}.[/red]")