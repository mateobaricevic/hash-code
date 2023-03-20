import copy
import glob
import parser
from argparse import ArgumentParser

import scorer
import solver
import writer

argument_parser = ArgumentParser()
argument_parser.add_argument("file_names", nargs="?", default="input/*")
args = argument_parser.parse_args()


for file_name in glob.glob(args.file_names):
    dataset = parser.parse(file_name)
    max_score = 0
    for path in dataset["cars"]:
        length = sum([dataset["streets"][street]["length"] for street in path[1:]])
        max_score += dataset["points"] + dataset["duration"] - length

    solution = solver.solve(dataset)
    score, red_lights = scorer.score(solution, dataset)

    best_score = 0
    best_solution = copy.deepcopy(solution)
    found_better = True
    while True:
        if not found_better or best_score == max_score:
            break
        found_better = False
        solution = copy.deepcopy(best_solution)
        for _ in range(16):
            if score > best_score:
                best_score = int(score)
                best_solution = copy.deepcopy(solution)
                found_better = True
                break

            max_amount = max(
                [
                    amount
                    for intersection in red_lights.values()
                    for amount in intersection.values()
                ]
            )
            for intersection, red_light in red_lights.items():
                for street, amount in red_light.items():
                    if amount > max_amount - max_amount * 0.02:
                        for schedule in solution[intersection]:
                            if schedule[0] == street:
                                schedule[1] += 1

            score, red_lights = scorer.score(solution, dataset)

            print(
                f"{file_name} | {score}/{max_score} ({max_score - score} to perfect score)"
                + " " * 10,
                end="\r",
            )
    print(
        f"{file_name} | {best_score}/{max_score} ({max_score - best_score} to perfect score)"
    )
    writer.write(best_solution, file_name.replace("input", "output"))
