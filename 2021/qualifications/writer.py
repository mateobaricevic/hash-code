
def write(solution, file_name):
    with open(file_name, 'w') as file:
        file.write(str(len(solution)) + '\n')
        for intersection_id, schedule in solution.items():
            file.write(str(intersection_id) + '\n')
            file.write(str(len(schedule)) + '\n')
            for cycle in schedule:
                cycle = map(str, cycle)
                file.write(' '.join(cycle) + '\n')
