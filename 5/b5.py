class Product:
    def __init__(self, pid, name, price, source):
        self.pid = pid
        self.name = name
        self.price = price
        self.source = source

    def display(self):
        print(f"ID: {self.pid}, Name: {self.name}, Price: {self.price}, Source: {self.source}")

products = []

def add_product():
    pid = input("Nhap ID: ")
    name = input("Nhap ten san pham: ")
    price = float(input("Nhap gia: "))
    source = input("Nhap nguon goc: ")
    products.append(Product(pid, name, price, source))
    print("Da them san pham thanh cong.")

def show_products():
    if not products:
        print("Danh sach san pham trong.")
    else:
        print("\n--- Danh sach san pham ---")
        for p in products:
            p.display()

def filter_products():
    try:
        max_price = float(input("Nhap gia de loc (chi giu san pham co gia < gia nay): "))
        filtered = [p for p in products if p.price < max_price]
        if filtered:
            print(f"\n--- Cac san pham co gia nho hon {max_price} ---")
            for p in filtered:
                p.display()
        else:
            print("Khong co san pham nao phu hop.")
    except ValueError:
        print("Gia khong hop le.")

def update_product():
    pid = input("Nhap ID san pham can cap nhat: ")
    for p in products:
        if p.pid == pid:
            p.name = input("Nhap ten moi: ")
            p.price = float(input("Nhap gia moi: "))
            p.source = input("Nhap nguon goc moi: ")
            print("Da cap nhat san pham.")
            return
    print("Khong tim thay san pham.")

def delete_product():
    pid = input("Nhap ID san pham can xoa: ")
    for p in products:
        if p.pid == pid:
            products.remove(p)
            print("Da xoa san pham.")
            return
    print("Khong tim thay san pham.")

def menu():
    while True:
        print("\n===== MENU =====")
        print("1. Them san pham")
        print("2. Hien thi danh sach san pham")
        print("3. Loc san pham theo gia")
        print("4. Cap nhat san pham")
        print("5. Xoa san pham")
        print("6. Thoat")

        choice = input("Chon chuc nang (1-6): ")
        if choice == '1':
            add_product()
        elif choice == '2':
            show_products()
        elif choice == '3':
            filter_products()
        elif choice == '4':
            update_product()
        elif choice == '5':
            delete_product()
        elif choice == '6':
            print("Dang thoat chuong trinh. Tam biet!")
            break
        else:
            print("Lua chon khong hop le. Vui long chon tu 1-6.")

menu()
