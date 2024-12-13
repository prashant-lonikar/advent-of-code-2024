import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# import a local txt file and print first few characters
with open("input.txt", "r") as file:
    data = file.read()

row = 0
switch = False
list_1 = []
list_2 = []
temp_char = ""

list_1 = []
list_2 = []
for line in data.splitlines():
    list_1.append(int(line.split("   ")[0]))
    list_2.append(int(line.split("   ")[1]))

list_1 = sorted(list_1)
list_2 = sorted(list_2)

distances = 0
for i in range(len(list_1)):
    distances += abs(list_1[i] - list_2[i])

print(distances)
