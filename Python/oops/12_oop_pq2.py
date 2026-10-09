class Book:

    title = "Harry Potter"
    author = "J.K. Rowling"
    list_of_review = []
    count = 0

    def __init__(self, reviewer_name):

        self.reviewer_name = reviewer_name

    def add_Review(self):

        Book.list_of_review.append(self.reviewer_name) 
        Book.count +=1
        print("Review added!")
    @classmethod
    def count_review(cls):
        print(f"Total reviewss = {Book.count}")
    @classmethod
    def display_reviews(cls):

        print(Book.list_of_review)

r1 = Book("Harshit")
r2 = Book("Siguu")

r1.add_Review()
r2.add_Review()
Book.display_reviews()
