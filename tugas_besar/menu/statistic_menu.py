from services.statistic_service import (
    best_selling_products,
    discounted_products_sales,
    low_stock_products,
    revenue_chart
)
from rich import print


def statistic_menu():
    while True:
        # print("\n" + "="*60)
        print("[bold cyan]STATISTIK TOKO[/bold cyan]")
        # print("="*60)
        print("[yellow]1. Tampilkan Semua Statistik[/yellow]")
        print("[yellow]0. Kembali ke Menu Utama[/yellow]")
        
        choice = input("[cyan]Pilih Menu: [/cyan]")
        
        if choice == "1":
            print("\n[bold cyan]Menampilkan Semua Statistik...[/bold cyan]\n")
            
            print("[bold]1. Product Paling Laku[/bold]")
            # print("-" * 60)
            best_selling_products()
            
            print("\n[bold]2. Penjualan Product Diskon[/bold]")
            # print("-" * 60)
            discounted_products_sales()
            
            print("\n[bold]3. Product dengan Stock Hampir Habis[/bold]")
            # print("-" * 60)
            low_stock_products()
            
            print("\n[bold]4. Grafik Omset Penjualan[/bold]")
            # print("-" * 60)
            revenue_chart()
        elif choice == "0":
            print("Kembali ke Menu Utama...")
            break
        else:
            print("[red]Pilihan tidak valid. Silakan coba lagi.[/red]")
     