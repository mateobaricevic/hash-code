import copy
import operator
import time
from datetime import timedelta


def solve(dataset, file_name):
    start = time.time()
    libraries = list(copy.deepcopy(dataset['libraries']).values())
    books = copy.deepcopy(dataset['books'])

    books.sort(key=operator.itemgetter('score'), reverse=True)
    libraries.sort(key=operator.itemgetter('n_books'), reverse=True)
    libraries.sort(key=operator.itemgetter('n_ship'), reverse=True)
    libraries.sort(key=operator.itemgetter('signup'))

    signup_times = {
        library['id']: sum(
            [library['signup'] for library in libraries[: index + 1]]
        )
        for index, library in enumerate(libraries)
    }

    solution = [{'id': library['id'], 'book_ids': []} for library in libraries]
    for progress, book in enumerate(books):
        for library in libraries:
            if book['id'] in library['book_ids']:
                s = [l for l in solution if l['id'] == library['id']][0]
                scanning_time = len(s['book_ids']) / library['n_ship']
                scanning_step = 1 / library['n_ship']
                if (
                    signup_times[library['id']] + scanning_time + scanning_step
                    < dataset['days']
                ):
                    s['book_ids'].append(book['id'])
                    break
        if progress % 10 == 0 or progress == len(books):
            print(
                f'{file_name} | Solving... {progress/len(books)*100:.1f}% '
                + f'({str(timedelta(seconds=time.time() - start))[:7]})'
                + ' ' * 10,
                end='\r',
            )
    return [library for library in solution if len(library['book_ids']) > 0]
