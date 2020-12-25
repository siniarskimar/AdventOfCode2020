def load_input():
    cases = open("input.txt", "r").readlines()
    for i in range(len(cases)):
        cases[i] = cases[i].replace('\n','')
    return cases

groups = []

def parse_input():
    inp = load_input()
    inp_len = len(inp)
    group = []
    for i in range(inp_len):
        line = inp[i]
        if line == '' and len(group) != 0:
            groups.append(group)
            group = []
        elif len(line) != 0:
            group.append(line)
    if len(group) != 0:
        groups.append(group)

def count_group(group):
    answer_set = set()
    group_len = len(group)
    for i in range(group_len):
        answer_set.update(group[i])
    return len(answer_set)

parse_input()

sum_count = 0
for i in range(len(groups)):
    sum_count += count_group(groups[i])

print(sum_count)

# print(groups)