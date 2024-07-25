class BookEntity:
    def __init__(self, BookDAO):
        self.data_access = BookDAO

    def list_books(self):
        return self.data_access.list()

    def get_book(self, book_id):
        return self.data_access.get_by_id(book_id)

    def add_book(self, title, author, summary):
        book_data = {
            "name": title,
            "author": author,
            "summary": summary
        }
        self.data_access.add(book_data)

    def update_book(self, book_id, title, author, summary):
        book_data = {
            "name": title,
            "author": author,
            "summary": summary
        }
        self.data_access.update(book_id, book_data)

    def delete_book(self, book_id):
        self.data_access.delete(book_id)
