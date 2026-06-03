from database.data import products, promotions

# Import Rich library untuk mempercantik tampilan output di terminal
from rich.table import Table

from rich import print



def add_promotion(sku, discount_percent): #Menambahkan promosi baru dengan validasi SKU dan diskon
    for product in products:
        if product["sku"] == sku:

            # Cek apakah sudah ada promo
            for promo in promotions:
                if promo["sku"] == sku:
                    print("SKU promosi sudah digunakan.")
                    return

            price = product["price"]
            harga_diskon = price * (1 - discount_percent / 100)

            # Simpan harga asli sebelum mengubah harga
            product["original_price"] = price
            # Harga yang ditampilkan berubah
            product["price"] = harga_diskon

            promotions.append({
                "sku": sku,
                "discount": discount_percent
            })

            print(f"Diskon {discount_percent}% berhasil ditambahkan")
            print(f"Harga asli : Rp{price:,.0f}")
            print(f"Harga setelah diskon : Rp{harga_diskon:,.0f}")
            return

    print("Produk tidak ditemukan.")


def view_promotions():  #Menampilkan semua promosi yang tersedia dengan informasi produk terkait
    if not promotions:
        print("[yellow]Tidak ada promosi yang tersedia.[/yellow]")
        return

    table = Table(title="Available Promotions")

    table.add_column("Product Name", style="blue")
    table.add_column("SKU", style="magenta")
    table.add_column("Original Price", style="green")
    table.add_column("Current Price", style="cyan")
    table.add_column("Discount (%)", style="red")

    for promo in promotions:

        product = next(
            (p for p in products if p["sku"] == promo["sku"]),
            None
        )

        if product:

            harga_asli = product.get("original_price", product["price"])
            harga_sekarang = product["price"]

            table.add_row(
                product["product_name"],
                product["sku"],
                f"Rp {harga_asli:,.0f}",
                f"Rp {harga_sekarang:,.0f}",
                f"{promo['discount']}%"
            )

    print(table)
    

def update_promotion(): #Memperbarui informasi promosi berdasarkan ID promosi
    sku = input("Enter SKU of the product to update: ")

    for promo in promotions:
        if promo["sku"] == sku:
            new_discount = int(input("Enter new discount percentage: "))
            promo["discount"] = new_discount
            print(f"Promotion for SKU {sku} has been updated.")
            return

    print(f"[red]No promotion found with SKU {sku}.[/red]")


def delete_promotion():  #Menghapus promosi berdasarkan ID promosi
    sku = input("Enter SKU of the promotion to delete: ")

    for i, promo in enumerate(promotions):
        if promo["sku"] == sku:
            del promotions[i]
            print(f"Promotion for SKU {sku} has been deleted.")
            return

    print(f"[red]No promotion found with SKU {sku}.[/red]")
    

def search_promotions():  #Mencari promosi berdasarkan nama produk atau ID promosi
    keyword = input("Enter product name or SKU to search: ")
    found_promotions = [promo for promo in promotions if keyword.lower() in promo["sku"].lower()]

    if found_promotions:
        for promo in found_promotions:
            product = next((p for p in products if p["sku"] == promo["sku"]), None)
            if product:
                print(f"|Product Name: {product['product_name']}, |SKU: {product['sku']}, |Price: {product['price']:,.0f}, |Discount: {promo['discount']}%|")
    else:
        print("[red]No promotions found matching the keyword.[/red]")