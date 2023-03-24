def write(solution, file_name):
    with open(file_name, 'w') as file:
        file.write(str(len(solution)) + '\n')
        for library in solution:
            file.write(str(library['id']) + ' ' + str(len(library['book_ids'])) + '\n')
            file.write(' '.join(map(str, library['book_ids'])) + '\n')
