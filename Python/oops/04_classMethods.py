class Laptop:
    storage_type  = "ssd"

    def __init__(self , RAM , storage):
        self.RAM = RAM
        self.storage = storage 

    def get_info(self): #instance method
        print(f"The laptop has {self.RAM} RAM & {self.storage} {self.storage_type}") #Object method can access class Attribute

    @classmethod
    def get_storage_type(cls):
        print(f"Storage type = {cls.storage_type} ") #class method cannot access the Object attribute 

    @staticmethod
    def calc_discount(price,discount):
        final_price = price-(price*discount/100)
        print(f"The discounter price is {final_price}")
    


l1 = Laptop("32 GB" , "1 TB")
l2 = Laptop("16 GB" , "1.5 TB")


# l1.get_info()
l1.get_storage_type()

l1.calc_discount(40_000 , 10)