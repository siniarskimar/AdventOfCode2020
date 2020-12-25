cases = open("input.txt", "r").readlines()
n_cases = len(cases)

for i in range(n_cases):
    cases[i] = cases[i].replace('\n','')

for i in range(n_cases):
    case = cases[i]
    cases[i] = case.replace("B", "1").replace("R", "1").replace("F", "0").replace("L", "0")

max_sid = 0
for i in range(n_cases):
    case = cases[i]
    row_id = int(case[0:7],2)
    column_id = int(case[7:10],2)
    seat_id = (row_id << 3) + column_id
    if seat_id > max_sid:
        max_sid = seat_id
print(max_sid)