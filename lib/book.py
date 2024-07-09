class Book:
    def __init__(self, title, page_count, author=None):
        self.title = title
        self.author = author
        self.page_count = page_count  # Use the property setter for validation
    
    @property
    def page_count(self):
        """Get the number of pages in the book."""
        return self._page_count
    
    @page_count.setter
    def page_count(self, page_count):
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print('Flipping the page...wow, you read fast!')
