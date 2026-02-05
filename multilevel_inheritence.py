class Product:
    def __init__(self,product_name,price):
        self.product_name=product_name
        self.price=price

    def display_product(self):
        print("product name is:",self.product_name)
        print("product name is:",self.price)

class ElectronicProduct(Product):
    def __init__(self,brand,warranty,product_name,price):
        self.brand=brand
        self.warranty=warranty
        super().__init__(product_name,price)

    def display_electronic_product(self):
        print("product name is:",self.product_name)
        print("product price is:",self.price)
        print("product brand is:",self.brand)
        print("product warranty is:",self.warranty)

class MobilePhone(ElectronicProduct):
    def __init__(self,ram,storage,brand,warranty,product_name,price):
        self.ram=ram
        self.storage=storage
        super().__init__(brand,warranty,product_name,price)

    def display_mobile_details(self):
        print("product ram is:",self.ram)
        print("product storage is:",self.storage)
        print("product name is:",self.product_name)
        print("product name is:",self.price)
        print("product brand is:",self.brand)
        print("product warranty is:",self.warranty)

mobilephone1=MobilePhone("2gb","128s","mani","2years","qwerty","2000$")
# mobilephone1.display_mobile_details()
mobilephone1.display_electronic_product()

