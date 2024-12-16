with open("day5_input_rules.txt", "r") as file:
    combined_file = file.read()

rules = combined_file.split("\n\n")[0]
data = combined_file.split("\n\n")[1]

# Part 1

rules_set = {}

for rule in rules.splitlines():
    left, right = int(rule.split("|")[0]), int(rule.split("|")[1])
    rules_set[right] = []

for rule in rules.splitlines():
    left, right = int(rule.split("|")[0]), int(rule.split("|")[1])
    (rules_set[right]).append(left)

updated_data = []
for row in data.splitlines():
    updated_data.append([int(x) for x in row.split(",")])

line_valid = True
middle_num = 0
total_sum = 0

for i, row in enumerate(updated_data):
    print(f"Current row: {row}")

    for j, current_num in enumerate(row):
        print(f"\tCurrent number: {current_num}. j = {j}")
        if current_num in rules_set.keys():
            predecessors_of_current_num = rules_set[
                int(current_num)
            ]  # this is a list of numbers that should be before current num
            for k in range(
                j + 1, len(row)
            ):  # check for each character after the current character
                print(f"Looking at {row[k]}")
                if (
                    row[k] in predecessors_of_current_num and row[k] not in row[0:j]
                ):  # i.e. check if there is a predecessors of row[j] after j but not before. I am doing the "after j" indexing in the k-for loop itself
                    print(f"{row[k]} is supposed to be before {row[j]}")
                    line_valid = False
                    print(
                        f"\tRow is invalid because the rule is {row[k]}|{row[j]} but {row[k]} appears after {row[j]} but not before."
                    )
                    break
            if line_valid == False:
                break
        else:
            print(f"\t\t--{current_num}: NO PREDECESSORS--")
            line_valid = True
    if line_valid:
        middle_num = row[int(len(row) / 2)]
        print(f"\tRow is valid. Middle number: {middle_num}")
    else:
        middle_num = 0
        line_valid = True
    total_sum += middle_num

print(total_sum)
