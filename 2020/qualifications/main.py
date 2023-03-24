import glob
import parser
from argparse import ArgumentParser

import scorer
import solver
import writer

argument_parser = ArgumentParser()
argument_parser.add_argument('file_names', nargs='?', default='input/*')
args = argument_parser.parse_args()

file_names = sorted(glob.glob(args.file_names))

for file_name in file_names:
    dataset = parser.parse(file_name)
    max_score = sum([book['score'] for book in dataset['books']])
    solution = solver.solve(dataset)
    score = scorer.score(solution, dataset)
    print(
        f'{file_name} | {score:,}/{max_score:,} ({max_score - score:,} to perfect score)'
    )
    writer.write(solution, file_name.replace('input', 'output'))
