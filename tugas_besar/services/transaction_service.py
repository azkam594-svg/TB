from rich.table import Table

from database.data import transactions, products
from rich import print
import datetime
import csv
import os
from pathlib import Path


def add_transaction(sku, quantity, date):
    # Validasi SKU
    product = next((p for p in products if p["sku"] == sku), None)
    if not product:
        print("[red]SKU tidak ditemukan di database produk.[/red]")
        return
    
    # Validasi quantity
    if quantity <= 0:
        print("[red]Quantity harus lebih dari 0.[/red]")
        return
    
    # Validasi stock
    if product["stock"] < quantity:
        print(f"[red]Stok tidak cukup. Stok tersedia: {product['stock']}[/red]")
        return
    
    transaction_id = f"T{len(transactions) + 1:03d}"
    amount = product["price"] * quantity

    transaction = {
        "transaction_id": transaction_id,
        "sku": sku,
        "quantity": quantity,
        "date": date,
        "amount": amount
    }
    
    # Kurangi stock
    product["stock"] -= quantity
    
    transactions.append(transaction)
    print(f"[green]Transaction {transaction_id} added successfully.[/green]")
    print(f"Amount: Rp {amount:,.0f}")

def view_transactions():
    if not transactions:
        print("[yellow]No transactions found.[/yellow]")
        return

    table = Table(title="Transactions")
    table.add_column("Transaction ID", style="cyan")
    table.add_column("SKU", style="magenta")
    table.add_column("Quantity", style="green")
    table.add_column("Date", style="blue")
    table.add_column("Amount", style="yellow")

    for t in transactions:
        table.add_row(t["transaction_id"], t["sku"], str(t["quantity"]), t["date"], f"Rp {t['amount']:,.0f}")
    print(table)

def delete_transaction():
    transaction_id = input("Enter Transaction ID to delete: ")
    for i, t in enumerate(transactions):
        if t["transaction_id"] == transaction_id:
            # Kembalikan stock
            product = next((p for p in products if p["sku"] == t["sku"]), None)
            if product:
                product["stock"] += t["quantity"]
            del transactions[i]
            print(f"[green]Transaction {transaction_id} deleted successfully.[/green]")
            return
    print(f"[red]Transaction ID {transaction_id} not found.[/red]")


def saldo_transaction():
    total_saldo = sum(t["amount"] for t in transactions)
    print(f"[green]Total Saldo: Rp {total_saldo:,.0f}[/green]")


def laporan_transaction():
    if not transactions:
        print("[red]No transactions to generate report.[/red]")
        return
    
    # Buat folder reports jika belum ada
    reports_dir = "reports"
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)
    
    # Generate filename dengan timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{reports_dir}/laporan_transaksi_{timestamp}.csv"
    
    # Hitung total
    total_amount = sum(t["amount"] for t in transactions)
    
    try:
        # Simpan ke CSV
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Transaction ID', 'SKU', 'Quantity', 'Date', 'Amount (Rp)']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Tulis header
            writer.writeheader()
            
            # Tulis data transaksi
            for t in transactions:
                writer.writerow({
                    'Transaction ID': t['transaction_id'],
                    'SKU': t['sku'],
                    'Quantity': t['quantity'],
                    'Date': t['date'],
                    'Amount (Rp)': f"{t['amount']:,.0f}"
                })
            
            # Tulis total
            writer.writerow({})
            writer.writerow({
                'Transaction ID': 'TOTAL',
                'SKU': '',
                'Quantity': '',
                'Date': '',
                'Amount (Rp)': f"{total_amount:,.0f}"
            })
        
        # Tampilkan pesan sukses
        full_path = os.path.abspath(filename)
        print(f"[green]✓ Report berhasil disimpan![/green]")
        print(f"[cyan]File: {full_path}[/cyan]")
        print(f"[yellow]Total Transaksi: {len(transactions)}[/yellow]")
        print(f"[yellow]Total Saldo: Rp {total_amount:,.0f}[/yellow]")
        
        # Tampilkan preview
        print("\n[bold]Preview Data:[/bold]")
        table = Table(title=f"Laporan Transaksi ({timestamp})")
        table.add_column("Transaction ID", style="cyan")
        table.add_column("SKU", style="magenta")
        table.add_column("Quantity", style="green")
        table.add_column("Date", style="blue")
        table.add_column("Amount", style="yellow")
        
        for t in transactions:
            table.add_row(t["transaction_id"], t["sku"], str(t["quantity"]), t["date"], f"Rp {t['amount']:,.0f}")
        
        print(table)
        
    except Exception as e:
        print(f"[red]Error saat menyimpan report: {str(e)}[/red]")

