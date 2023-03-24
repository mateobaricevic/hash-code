def parse(file_name):
    with open(file_name) as file:
        b, l, days = map(int, file.readline().split())
        books = list(map(int, file.readline().split()))
        books = [
            {
                'id': id,
                'score': score
            } for id, score in enumerate(books)
        ]
        libraries = {}
        for id in range(l):
            n_books, signup_time, n_shipping = file.readline().split()
            book_ids = list(map(int, file.readline().split()))
            libraries[id] = {
                'id': id,
                'n_books': int(n_books),
                'signup_time': int(signup_time),
                'n_shipping': int(n_shipping),
                'book_ids': book_ids,
            }
        return {
            'b': b,
            'l': l,
            'days': days,
            'books': books,
            'libraries': libraries,
        }
