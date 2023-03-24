import copy
import operator
import time
from datetime import timedelta


def solve(dataset):
    start = time.time()
    libraries = list(copy.deepcopy(dataset['libraries']).values())
    books = copy.deepcopy(dataset['books'])

    books.sort(key=operator.itemgetter('score'), reverse=True)
    libraries.sort(key=operator.itemgetter('n_shipping'), reverse=True)
    libraries.sort(key=operator.itemgetter('signup_time'))

    signup_times = {
        library['id']: sum(
            [library['signup_time'] for library in libraries[: index + 1]]
        )
        for index, library in enumerate(libraries)
    }

    solution = [{'id': library['id'], 'book_ids': []} for library in libraries]
    for progress, book in enumerate(books):
        for i, library in enumerate(libraries):
            if book['id'] not in library['book_ids']:
                continue
            scanning_time = len(solution[i]['book_ids']) / library['n_shipping']
            scanning_step = 1 / library['n_shipping']
            if (
                signup_times[library['id']] + scanning_time + scanning_step
                < dataset['days']
            ):
                solution[i]['book_ids'].append(book['id'])
                break
        print(
            f'Solving... {progress/len(books)*100:.2f}% {str(timedelta(seconds=time.time() - start))[:7]}'
            + ' ' * 10,
            end='\r',
        )
    return [library for library in solution if len(library['book_ids']) > 0]
