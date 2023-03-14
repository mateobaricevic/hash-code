import glob

import parser, solver, scorer, writer

for file_name in glob.glob('input/*'):
    dataset = parser.parse(file_name)
    solution = solver.solve(dataset)
    score = scorer.score(solution, dataset)
    writer.write(solution, file_name.replace('input', 'output'))

    max_score = 0
    for path in dataset['cars']:
        travel_length = sum([dataset['streets'][street]['length'] for street in path[1:]])
        max_score += dataset['points'] + dataset['duration'] - travel_length
    print(f"{file_name} | {score}/{max_score} ({max_score - score} to perfect score)")
