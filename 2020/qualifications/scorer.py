import copy
from datetime import timedelta
from time import time as timing


def score(solution, dataset):
    start = timing()
    days = dataset['days']
    books = dataset['books']
    libraries = dataset['libraries']
    solution = copy.deepcopy(solution)

    signup_times = {}
    for index, library in enumerate(solution):
        if index > 0:
            signup_times[library['id']] = (
                signup_times[solution[index - 1]['id']]
                + libraries[library['id']]['signup_time']
            )
        else:
            signup_times[library['id']] = libraries[library['id']]['signup_time']

    time = score = 0
    scanned = [False for _ in range(len(books))]
    while time < days:
        for library in solution:
            if time > signup_times[library['id']]:
                for _ in range(libraries[library['id']]['n_shipping']):
                    if len(library['book_ids']) == 0:
                        break
                    book_id = library['book_ids'].pop(0)
                    if not scanned[book_id]:
                        score += books[book_id]['score']
                        scanned[book_id] = True
        time += 1
        print(
            f'Scoring... {time/days*100:.2f}% {str(timedelta(seconds=timing() - start))[:7]}'
            + ' ' * 10,
            end='\r',
        )
    return score
