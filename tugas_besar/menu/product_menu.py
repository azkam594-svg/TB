from services.product_service import add_product, view_products, search_products, update_product, delete_product

def product_menu(): #Menu untuk manage products
    while True:
        print("= MANAGE PRODUCTS =")
        print("1. Add Product")
        print("2. View Products")
        print("3. Search Products")
        print("4. Update Product")
        print("5. Delete Product")
        print("0. Back to Main Menu")
        choice = input("Select an option: ")
        
        if choice == '1':
            product_name = input("Enter product name: ")
            sku = input("Enter SKU: ")
            price = float(input("Enter price: "))
            stock = int(input("Enter stock: "))
            add_product(product_name, sku, price, stock)
            
        elif choice == '2':
            view_products() 
        
        elif choice == '3':
            search_products()
            
        elif choice == '4':
            update_product()
            
        elif choice == '5':
            delete_product()
            
        elif choice == '0':
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid option. Please try again.")