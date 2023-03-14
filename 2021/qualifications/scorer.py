import copy


def score(solution, dataset):
    streets = dataset["streets"]
    duration = dataset["duration"]
    cars = copy.deepcopy(dataset["cars"])

    cycles = [[] for _ in range(dataset["i"])]
    for intersection, schedule in solution.items():
        for cycle in schedule:
            cycles[intersection] += [cycle[0] for _ in range(cycle[1])]

    queues = [{} for _ in range(dataset["i"])]
    for street_name, street in streets.items():
        intersection = street["end"]
        queues[intersection][street_name] = []

    travelling = [0 for _ in cars]
    for car, path in enumerate(cars):
        street_name = path[0]
        intersection = streets[street_name]["end"]
        queues[intersection][street_name].append(car)
        path.pop(0)

    score = 0
    time = 0
    while time < duration:
        for intersection in range(dataset["i"]):
            if len(cycles[intersection]) == 0:
                continue

            cycle = cycles[intersection]
            queue = queues[intersection][cycle[time % len(cycle)]]

            if len(queue) > 0 and not travelling[queue[0]]:
                car = queue.pop(0)
                street_name = cars[car].pop(0)
                street_length = streets[street_name]["length"]
                intersection = streets[street_name]["end"]

                if len(cars[car]) == 0:
                    if time + street_length <= duration:
                        score += dataset["points"] + duration - time
                    break

                travelling[car] += street_length
                queues[intersection][street_name].append(car)
                break
        travelling = [t - 1 if t > 0 else t for t in travelling]
        time += 1
    return score
