import logging
import time

logging.basicConfig(level=logging.DEBUG)

with open("day2_input.txt", "r") as file:
    data = file.read()

# Part 1

input_set = {}
trend = ""
current_row = []
row_category = ""
safe_row_count = 0

for line in data.splitlines():
    current_row = [int(x) for x in line.split(" ")]
    if current_row[0] < current_row[-1]:
        trend = "increasing"
        for i in range(len(current_row) - 1):
            if (
                current_row[i + 1] - current_row[i] >= 1
                and current_row[i + 1] - current_row[i] <= 3
            ):
                row_category = "safe"
            else:
                row_category = "unsafe"
                break
        if row_category == "safe":
            safe_row_count += 1
    else:
        trend = "decreasing"
        for i in range(len(current_row) - 1):
            if (
                current_row[i] - current_row[i + 1] >= 1
                and current_row[i] - current_row[i + 1] <= 3
            ):
                row_category = "safe"
            else:
                row_category = "unsafe"
                break
        if row_category == "safe":
            safe_row_count += 1

print("Safe rows in part 1:", safe_row_count)


# Part 2
safe_row_count = 0  # Reset counter for part 2

for line in data.splitlines():
    current_row = [int(x) for x in line.split(" ")]
    logging.debug(f"Row: {current_row}")

    if current_row[0] < current_row[-1]:
        trend = "increasing"
        for i in range(len(current_row) - 1):
            if (
                current_row[i + 1] - current_row[i] >= 1
                and current_row[i + 1] - current_row[i] <= 3
            ):
                row_category = "safe"
            else:
                logging.debug(f"Initially unsafe")
                for j in range(len(current_row)):
                    modified_current_row = current_row[:j] + current_row[j + 1 :]
                    modified_row_category = "safe"

                    for k in range(len(modified_current_row) - 1):
                        if not (
                            modified_current_row[k + 1] - modified_current_row[k] >= 1
                            and modified_current_row[k + 1] - modified_current_row[k]
                            <= 3
                        ):
                            modified_row_category = "unsafe"
                            break

                    if modified_row_category == "safe":
                        row_category = "safe"
                        logging.debug(f"Made safe by removing {current_row[j]}")
                        break
                    elif j == len(current_row) - 1:
                        row_category = "unsafe"
                        logging.debug("No removal makes this row safe")
                break
        if row_category == "safe":
            safe_row_count += 1
            logging.debug(f"Safe row count: {safe_row_count}")

    else:
        # Similar structure for decreasing trend
        trend = "decreasing"
        for i in range(len(current_row) - 1):
            if (
                current_row[i] - current_row[i + 1] >= 1
                and current_row[i] - current_row[i + 1] <= 3
            ):
                row_category = "safe"
            else:
                logging.debug(f"Initially unsafe")
                for j in range(len(current_row)):
                    modified_current_row = current_row[:j] + current_row[j + 1 :]
                    modified_row_category = "safe"

                    for k in range(len(modified_current_row) - 1):
                        if not (
                            modified_current_row[k] - modified_current_row[k + 1] >= 1
                            and modified_current_row[k] - modified_current_row[k + 1]
                            <= 3
                        ):
                            modified_row_category = "unsafe"
                            break

                    if modified_row_category == "safe":
                        row_category = "safe"
                        logging.debug(f"Made safe by removing {current_row[j]}")
                        break
                    elif j == len(current_row) - 1:
                        row_category = "unsafe"
                        logging.debug("No removal makes this row safe")
                break
        if row_category == "safe":
            safe_row_count += 1
            logging.debug(f"Safe row count: {safe_row_count}")

print("Safe rows in part 2:", safe_row_count)
