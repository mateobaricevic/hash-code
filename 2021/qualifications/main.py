import glob
import parser
from argparse import ArgumentParser

import scorer
import solver
import writer

argument_parser = ArgumentParser()
argument_parser.add_argument("file_name")
args = argument_parser.parse_args()

file_names = glob.glob("input/*")
if args.file_name:
    file_names = [args.file_name]


for file_name in file_names:
    dataset = parser.parse(file_name)
    solution = solver.solve(dataset)
    score = scorer.score(solution, dataset)
    writer.write(solution, file_name.replace("input", "output"))

    max_score = 0
    for path in dataset["cars"]:
        travel_length = sum(
            [dataset["streets"][street]["length"] for street in path[1:]]
        )
        max_score += dataset["points"] + dataset["duration"] - travel_length
    print(
        f"{file_name} | {score}/{max_score} ({max_score - score} to perfect score)",
        end="\r",
    )