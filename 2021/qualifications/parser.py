def parse(file_name):
    with open(file_name) as file:
        duration, i, s, c, points = map(int, file.readline().split())
        streets = {}
        for _ in range(s):
            start, end, name, length = file.readline().split()
            streets[name] = {
                "start": int(start),
                "end": int(end),
                "length": int(length),
            }
        cars = []
        for _ in range(c):
            car = file.readline().split()
            cars.append(car[1:])
        return {
            "duration": duration,
            "i": i,
            "s": s,
            "c": c,
            "points": points,
            "streets": streets,
            "cars": cars,
        }
