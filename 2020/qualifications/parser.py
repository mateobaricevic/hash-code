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
        for library_id in range(l):
            n_books, signup, n_ship = file.readline().split()
            book_ids = list(map(int, file.readline().split()))
            libraries[library_id] = {
                'id': library_id,
                'n_books': int(n_books),
                'signup': int(signup),
                'n_ship': int(n_ship),
                'book_ids': book_ids,
            }
        return {
            'b': b,
            'l': l,
            'days': days,
            'books': books,
            'libraries': libraries,
        }
