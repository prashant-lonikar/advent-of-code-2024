import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# import a local txt file and print first few characters
with open("day1_input.txt", "r") as file:
    data = file.read()

# Part 1
list_1 = []
list_2 = []
for line in data.splitlines():
    list_1.append(int(line.split("   ")[0]))
    list_2.append(int(line.split("   ")[1]))

list_1 = sorted(list_1)
list_2 = sorted(list_2)

distance = 0
for i in range(len(list_1)):
    distance += abs(list_1[i] - list_2[i])

print("Distance: ", distance)

# Part 2
similarity_score = 0
for i in range(len(list_1)):
    count_of_number_in_list_2 = list_2.count(list_1[i])
    similarity_score += list_1[i] * count_of_number_in_list_2

print("Similarity score: ", similarity_score)
