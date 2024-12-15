with open("day3_input.txt", "r") as file:
    data = file.read()

# Part 1


def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


small_data = data[:]

potential_pair_counter = 0
good_pair_count = 0
final_sum = 0

current_substring_index = 0

string_so_far = ""
first_number = ""
second_number = ""
current_character = ""

for i, char in enumerate(small_data):
    string_so_far += char
    if string_so_far == "mul(":
        potential_pair_counter += 1
        numbers_within_mul = small_data[i + 1 :].split(")")
        try:
            first_number = numbers_within_mul[0].split(",")[0]
            second_number = numbers_within_mul[0].split(",")[1]
            if is_integer(first_number) and is_integer(second_number):
                good_pair_count += 1
                final_sum += int(first_number) * int(second_number)
                string_so_far = ""
                first_number = ""
                second_number = ""
            else:
                string_so_far = ""
                first_number = ""
                second_number = ""
        except:
            string_so_far = ""
            first_number = ""
            second_number = ""
        current_substring_index = 0
    elif (string_so_far + char)[current_substring_index] == "mul("[
        current_substring_index
    ]:
        current_substring_index += 1
    else:
        string_so_far = ""
        current_substring_index = 0

print(f"Part 1 answer: {final_sum}")

# Part 2

small_data = data[:]

activation_status = "DO"

final_sum_2 = 0

print(f"Small data: {small_data}")
for i, char in enumerate(small_data):
    string_so_far += char
    print(f"String so far: {string_so_far}")
    if string_so_far == "mul(" and activation_status == "DO":
        print("MUL + DO!")
        potential_pair_counter += 1
        numbers_within_mul = small_data[i + 1 :].split(")")
        try:
            first_number = numbers_within_mul[0].split(",")[0]
            second_number = numbers_within_mul[0].split(",")[1]
            if is_integer(first_number) and is_integer(second_number):
                good_pair_count += 1
                final_sum_2 += int(first_number) * int(second_number)
                print(f"New sum = {final_sum_2}")
                string_so_far = ""
                first_number = ""
                second_number = ""

            else:
                string_so_far = ""
                first_number = ""
                second_number = ""
        except:
            string_so_far = ""
            first_number = ""
            second_number = ""
        current_substring_index = 0
    elif string_so_far == "mul(" and activation_status == "DONT":
        print("MUL + DONT :(")
        string_so_far = ""
        first_number = ""
        second_number = ""
        current_substring_index = 0
    elif string_so_far == "do()":
        print("Status is now ACTIVE")
        activation_status = "DO"
        current_substring_index = 0
        string_so_far = ""
        first_number = ""
        second_number = ""
    elif string_so_far == "don't()":
        print("Status is now DEACTIVE")
        activation_status = "DONT"
        current_substring_index = 0
        string_so_far = ""
        first_number = ""
        second_number = ""
    elif (
        (string_so_far + char)[current_substring_index]
        == "mul(###"[
            current_substring_index
        ]  # Have to add padding because string index goes out of range due to dont
        or (string_so_far + char)[current_substring_index]
        == "do()###"[
            current_substring_index
        ]  # Have to add padding because string index goes out of range due to dont
        or (string_so_far + char)[current_substring_index]
        == "don't()"[current_substring_index]
    ):
        current_substring_index += 1
    else:
        string_so_far = ""
        current_substring_index = 0
        first_number = ""
        second_number = ""

print(f"Part 2 answer: {final_sum_2}")
