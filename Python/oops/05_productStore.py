class Store:

    count = 0
    def __init__(self, name,price):

        self.name = name
        self.price = price
        Store.count += 1

    @classmethod
    def get_count(cls):
        print(f"Total products created = {cls.count}")

    @staticmethod
    def discounted_price(discount , price):
        final_price = price-(price*discount/100)
        print(f"Discounter price = {final_price}")

prod1 = Store("LG Fully Automatic Washing Machine" , 25_000)
prod2 = Store("DigitalnWriting Pad" , 5003)

# Store.get_count()

prod1.discounted_price(10 , 5000)
        
