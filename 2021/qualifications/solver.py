def solve(dataset):
    streets = dataset["streets"]
    cars = dataset["cars"]
    i = dataset["i"]

    counts = [{street: 0 for street in streets} for _ in range(i)]
    for path in cars:
        for street in path:
            intersection = streets[street]["end"]
            counts[intersection][street] += 1

    return {
        intersection: [
            [street, 1] for street in streets if counts[intersection][street] > 0
        ]
        for intersection in range(i)
    }
