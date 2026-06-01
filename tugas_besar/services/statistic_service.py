from collections import defaultdict

from database.data import products, transactions, promotions

from rich import print

from rich.table import Table

from datetime import datetime

import matplotlib.pyplot as plt



def best_selling_products():  #Menampilkan product paling laku berdasarkan quantity terjual
    if not transactions:
        print("[yellow]Tidak ada data transaksi untuk ditampilkan.[/yellow]")
        return
    
    # Hitung jumlah penjualan per SKU
    sales_count = defaultdict(int)
    sales_amount = defaultdict(float)
    
    for t in transactions:
        sales_count[t["sku"]] += t["quantity"]
        sales_amount[t["sku"]] += t["amount"]
    
    if not sales_count:
        print("[yellow]Tidak ada penjualan yang tercatat.[/yellow]")
        return
    
    # Urutkan berdasarkan quantity terjual
    sorted_sales = sorted(sales_count.items(), key=lambda x: x[1], reverse=True)
    
    # Buat tabel
    table = Table(title="Product Paling Laku")
    table.add_column("Rank", style="bold cyan")
    table.add_column("SKU", style="magenta")
    table.add_column("Product Name", style="green")
    table.add_column("Qty Terjual", style="yellow")
    table.add_column("Total Revenue (Rp)", style="cyan")
    
    for rank, (sku, qty) in enumerate(sorted_sales, 1):
        product = next((p for p in products if p["sku"] == sku), None)
        product_name = product["product_name"] if product else "Unknown"
        revenue = sales_amount[sku]
        table.add_row(
            str(rank),
            sku,
            product_name,
            str(qty),
            f"{revenue:,.0f}"
        )
    
    print(table)
    

def discounted_products_sales():  #Menampilkan penjualan product yang sedang diskon
    if not transactions:
        print("[yellow]Tidak ada data transaksi untuk ditampilkan.[/yellow]")
        return
    
    if not promotions:
        print("[yellow]Tidak ada product yang sedang diskon.[/yellow]")
        return
    
    # Ambil SKU product yang diskon
    discounted_skus = {p["sku"]: p["discount"] for p in promotions}
    
    # Filter transaksi dengan product yang diskon
    discounted_sales = defaultdict(lambda: {"qty": 0, "amount": 0})
    
    for t in transactions:
        if t["sku"] in discounted_skus:
            discounted_sales[t["sku"]]["qty"] += t["quantity"]
            discounted_sales[t["sku"]]["amount"] += t["amount"]
    
    if not discounted_sales:
        print("[yellow]Tidak ada penjualan untuk product yang sedang diskon.[/yellow]")
        return
    
    # Urutkan berdasarkan amount
    sorted_sales = sorted(discounted_sales.items(), key=lambda x: x[1]["amount"], reverse=True)
    
    # Buat tabel
    table = Table(title="Penjualan Product Diskon")
    table.add_column("SKU", style="magenta")
    table.add_column("Product Name", style="green")
    table.add_column("Diskon (%)", style="red")
    table.add_column("Qty Terjual", style="yellow")
    table.add_column("Total Penjualan (Rp)", style="cyan")
    table.add_column("Harga Original (Rp)", style="blue")
    
    for sku, sales_data in sorted_sales:
        product = next((p for p in products if p["sku"] == sku), None)
        discount_pct = discounted_skus[sku]
        
        if product:
            original_price = product["price"]
            revenue = sales_data["amount"]
            table.add_row(
                sku,
                product["product_name"],
                f"{discount_pct}%",
                str(sales_data["qty"]),
                f"{revenue:,.0f}",
                f"{original_price:,.0f}"
            )
    
    print(table)


def low_stock_products():  #Menampilkan product dengan stock hampir habis (threshold bisa disesuaikan)
    # Tentukan threshold untuk low stock (20% dari stock awal atau misal < 5)
    low_stock_threshold = 5
    
    if not products:
        print("[yellow]Tidak ada data product.[/yellow]")
        return
    
    # Filter product dengan stock rendah
    low_stock_items = [p for p in products if p["stock"] <= low_stock_threshold]
    
    if not low_stock_items:
        print("[green]✓ Semua product memiliki stock yang cukup.[/green]")
        return
    
    # Urutkan berdasarkan stock
    low_stock_items.sort(key=lambda x: x["stock"])
    
    # Buat tabel
    table = Table(title="Product dengan Stock Hampir Habis")
    table.add_column("SKU", style="magenta")
    table.add_column("Product Name", style="green")
    table.add_column("Stock Saat Ini", style="red")
    table.add_column("Harga (Rp)", style="cyan")
    table.add_column("Status", style="yellow")
    
    for product in low_stock_items:
        stock = product["stock"]
        if stock == 0:
            status = "[red]HABIS[/red]"
        elif stock <= 2:
            status = "[red]SANGAT RENDAH[/red]"
        else:
            status = "[yellow]RENDAH[/yellow]"
        
        table.add_row(
            product["sku"],
            product["product_name"],
            str(stock),
            f"{product['price']:,.0f}",
            status
        )
    
    print(table)
    

def revenue_chart():  #Menampilkan grafik omset penjualan per product (bar chart) dan proporsi penjualan (pie chart)
    if not transactions:
        print("[red]Tidak ada data transaksi untuk membuat grafik.[/red]")
        return
    
    # Hitung omset per product
    product_revenue = defaultdict(float)
    product_qty = defaultdict(int)
    
    for t in transactions:
        product_revenue[t["sku"]] += t["amount"]
        product_qty[t["sku"]] += t["quantity"]
    
    if not product_revenue:
        print("[red]Tidak ada data omset yang tersedia.[/red]")
        return
    
    # Ambil nama product
    skus = list(product_revenue.keys())
    product_names = []
    for sku in skus:
        product = next((p for p in products if p["sku"] == sku), None)
        product_names.append(product["product_name"] if product else sku)
    
    revenues = [product_revenue[sku] for sku in skus]
    
    # Buat figure dengan 2 subplot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Grafik 1: Bar chart - Omset per Product
    colors = plt.cm.Set3(range(len(product_names)))
    ax1.bar(product_names, revenues, color=colors, edgecolor='black', linewidth=1.5)
    ax1.set_title("Omset Penjualan per Product", fontsize=14, fontweight='bold')
    ax1.set_xlabel("Product", fontsize=11)
    ax1.set_ylabel("Omset (Rp)", fontsize=11)
    ax1.grid(axis='y', alpha=0.3, linestyle='--')
    
    # Format y-axis sebagai currency
    ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'Rp {x/1e6:.1f}'))
    plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45, ha='right')
    
    # Grafik 2: Pie chart - Proporsi Penjualan
    colors_pie = plt.cm.Set2(range(len(product_names)))
    wedges, texts, autotexts = ax2.pie(
        revenues, 
        labels=product_names, 
        autopct='%1.1f%%',
        colors=colors_pie,
        startangle=90,
        textprops={'fontsize': 10}
    )
    
    # Format autopct untuk menampilkan nilai
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(9)
    
    ax2.set_title("Proporsi Penjualan", fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    
    # Simpan grafik
    try:
        import os
        if not os.path.exists("reports"):
            os.makedirs("reports")
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"reports/grafik_omset_{timestamp}.png"
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.show()
        
        print(f"[green]✓ Grafik berhasil disimpan di: {os.path.abspath(filename)}[/green]")
    except Exception as e:
        print(f"[red]Error saat menyimpan grafik: {str(e)}[/red]")
        plt.show()