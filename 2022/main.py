import sys

dataset = "a"
if len(sys.argv) > 1:
  dataset = sys.argv[1]

with open("input/" + dataset + ".in.txt") as file:
  lines = file.read().splitlines()

line = lines.pop(0).split(" ")
c = int(line[0])
p = int(line[1])

contributors = []
for i in range(c):
  line = lines.pop(0).split(" ")
  contributors.append({
    "name": line[0],
    "skills": []
  })
  for j in range(int(line[1])):
    line = lines.pop(0).split(" ")
    contributors[-1]["skills"].append({
      "name": line[0],
      "level": int(line[1])
    })
# print(contributors)

projects = []
for i in range(p):
  line = lines.pop(0).split(" ")
  projects.append({
    "name": line[0],
    "days": int(line[1]),
    "score": int(line[2]),
    "best_before": int(line[3]),
    "roles": [],
    "assignments": []
  })
  for j in range(int(line[4])):
    line = lines.pop(0).split(" ")
    projects[-1]["roles"].append({
      "name": line[0],
      "level": int(line[1])
    })
# print(projects)

for project in projects:
  for role in project["roles"]:
    has_skill = [c for c in contributors if role["name"] in [x["name"] for x in c["skills"]]]
    has_level = [c for c in has_skill if next(s for s in c["skills"] if s["name"] == role["name"])["level"] >= role["level"]]
    filtered = [c for c in has_level if c["name"] not in project["assignments"]]
    if len(filtered) == 0:
      project["assignments"] = []
      break
    project["assignments"].append(filtered[0]["name"])

projects = sorted(projects, key=lambda project: project["days"])
# print(projects)

with open("output/" + dataset + ".out.txt", "w") as file:
  file.write(str(sum([1 for project in projects if len(project["assignments"]) > 0])) + "\n")
  for project in projects:
    if len(project["assignments"]) > 0:
      file.write(project["name"] + "\n")
      file.write(" ".join(project["assignments"]) + "\n")
