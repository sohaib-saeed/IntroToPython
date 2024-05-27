class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def set_title (self,title):
        self.title = title
    def set_author(self,author):
        self.author = author
    def get_title(self):
        return self.title
    def get_author(self):
        return self.author
    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}"
class Fiction(Book):
    def __init__(self,title,author,reading_level):
        super().__init__(title,author)
        self.reading_level = reading_level
    def set_reading_level(self,reading_level):
        self.reading_level = reading_level
    def get_reading_level(self):
        return self.reading_level
    def __str__(self):
        return f"{super().__str__()}\n" + f"Reading Level: {self.reading_level}"
class NonFiction(Book):
    def __init__(self,title,author,no_of_pages):
        super().__init__(title,author)
        self.no_of_pages = no_of_pages
    def set_no_of_pages(self,no_of_pages):
        self.non_of_pages = no_of_pages
    def get_no_of_pages(self):
        return self.no_of_pages
    def __str__(self):
        return f"{super().__str__()}\n" + f"No of Pages: {self.no_of_pages}"
def main():
    f = Fiction("s", "s", 3)
    print(f)
    print("------------------")
    nf = NonFiction("s", "ss", 33)
    print(nf)
main()
