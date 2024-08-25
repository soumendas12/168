class Book:
    def __init__(self,name,author,price,publishing):
        self.book_name = name
        self.author_name = author
        self.book_price = price
        self.publishing_year = publishing
        
    def add_book(self):
        print("Book Name: "+self.book_name)
        print("Author Name: "+self.author_name)
        print("Book Price: "+self.book_price)
        print("Publishing Year: "+self.publishing_year)
        print("Book Added")
        
book1 = Book("Jujutsu Kaisen","Gege AKUTAMI","$11.99 $9.59","March 5, 2018")
book1.add_book()

book2 = Book("Death Note","Tsugumi Ohba","$49.99 $39.99", "December 1, 2003")
book2.add_book()