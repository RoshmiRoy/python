class publisher:
    def __init__(self):
        print("this is parent class")


class book(publisher):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print("title of the book is", self.title)
        print("author of the book is ", self.author)


class python(book):
    def __init__(self, price, no):
        self.price = price
        self.no = no

    def display(self):
        print("tha amount of this book is", self.price)
        print("total no of pages ", self.no)


p = book("Learning Python", "hussain")
p.display()
p = python(550, 852)
p.display()