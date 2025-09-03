class Book:
    def __init__(self, book_name, autherr):
        self.book_name = book_name
        self.auther = autherr
    def get_info(self):
        return f"book: {self.book_name}, auther: {self.auther.Auther}"
class Auther:
    def __init__(self, auther):
        self.auther = auther

a = Auther("alisher navoiy")
b = Book("xamsa", a)
print(b.get_info())
