with open("day4_input.txt", "r") as file:
    data = file.read()

data_matrix = []
for row in data.splitlines():
    data_matrix.append(list(row))

# Part 1

xmas_count = 0

for i, row in enumerate(data_matrix):
    print(f"Looking at row {i}:")
    for j, char in enumerate(row):
        if (
            char == "X"
        ):  # fixing the starting point to X otherwise we'll end up multi-counting

            print(f"\tX found at position {j}")

            # Type 1: Row-wise - Left to right
            try:
                if (
                    data_matrix[i][j + 1] == "M"
                    and data_matrix[i][j + 2] == "A"
                    and data_matrix[i][j + 3] == "S"
                ):
                    print("\t\tXMAS FOUND! Left to right!")
                    xmas_count += 1
                else:
                    print("\t\tXMAS NOT FOUND Left to right")
                    data_matrix[i][j] = "X"
            except:
                print("\t\tNot enough characters on the right")
                data_matrix[i][j] = "X"

            # Type 2: Row-wise - Right to left
            try:
                if (
                    data_matrix[i][j - 1] == "M"
                    and data_matrix[i][j - 2] == "A"
                    and data_matrix[i][j - 3] == "S"
                    and j - 3 >= 0
                ):
                    print("\t\tXMAS FOUND! Right to left!")
                    xmas_count += 1
                else:
                    print("\t\tXMAS NOT FOUND Right to left")
                    data_matrix[i][j] = "X"
            except:
                print("\t\tNot enough characters on the left")
                data_matrix[i][j] = "X"

            # Type 3: Column-wise - Top to bottom
            try:
                if (
                    data_matrix[i + 1][j] == "M"
                    and data_matrix[i + 2][j] == "A"
                    and data_matrix[i + 3][j] == "S"
                ):
                    print("\t\tXMAS FOUND! Top to bottom!")
                    xmas_count += 1
                else:
                    print("\t\tXMAS NOT FOUND Top to bottom")
                    data_matrix[i][j] = "X"
            except:
                print("\t\tNot enough characters below")
                data_matrix[i][j] = "X"

            # Type 4: Column-wise - Bottom to top
            try:
                if (
                    data_matrix[i - 1][j] == "M"
                    and data_matrix[i - 2][j] == "A"
                    and data_matrix[i - 3][j] == "S"
                    and i - 3 >= 0
                ):
                    print("\t\tXMAS FOUND! Bottom to top!")
                    xmas_count += 1
                else:
                    print("\t\tXMAS NOT FOUND Bottom to top")
                    data_matrix[i][j] = "X"
            except:
                print("\t\tNot enough characters above")
                data_matrix[i][j] = "X"

            # Type 5: Diagonal-wise - Bottomleft to Topright
            try:
                if (
                    data_matrix[i - 1][j + 1] == "M"
                    and data_matrix[i - 2][j + 2] == "A"
                    and data_matrix[i - 3][j + 3] == "S"
                    and i - 3 >= 0
                ):
                    print("\t\tXMAS FOUND! Bottomleft to Topright!")
                    xmas_count += 1
                else:
                    print("\t\tXMAS NOT FOUND Bottomleft to Topright")
                    data_matrix[i][j] = "X"
            except:
                print("\t\tNot enough characters in diagonal (Bottomleft to Topright)")
                data_matrix[i][j] = "X"

            # Type 6: Diagonal-wise - Topright to Bottomleft
            try:
                if (
                    data_matrix[i + 1][j - 1] == "M"
                    and data_matrix[i + 2][j - 2] == "A"
                    and data_matrix[i + 3][j - 3] == "S"
                    and j - 3 >= 0
                ):
                    print("\t\tXMAS FOUND! Topright to Bottomleft!")
                    xmas_count += 1
                else:
                    print("\t\tXMAS NOT FOUND Topright to Bottomleft")
                    data_matrix[i][j] = "X"
            except:
                print("\t\tNot enough characters in diagonal (Topright to Bottomleft)")
                data_matrix[i][j] = "X"

            # Type 7: Diagonal-wise - Bottomright to Topleft
            try:
                if (
                    data_matrix[i - 1][j - 1] == "M"
                    and data_matrix[i - 2][j - 2] == "A"
                    and data_matrix[i - 3][j - 3] == "S"
                    and i - 3 >= 0
                    and j - 3 >= 0
                ):
                    print("\t\tXMAS FOUND! Bottomright to Topleft!")
                    xmas_count += 1
                else:
                    print("\t\tXMAS NOT FOUND Bottomright to Topleft")
                    data_matrix[i][j] = "X"
            except:
                print("\t\tNot enough characters in diagonal (Bottomright to Topleft)")
                data_matrix[i][j] = "X"

            # Type 8: Diagonal-wise - Topleft to Bottomright
            try:
                if (
                    data_matrix[i + 1][j + 1] == "M"
                    and data_matrix[i + 2][j + 2] == "A"
                    and data_matrix[i + 3][j + 3] == "S"
                ):
                    print("\t\tXMAS FOUND! Topleft to Bottomright!")
                    xmas_count += 1
                else:
                    print("\t\tXMAS NOT FOUND Topleft to Bottomright")
                    data_matrix[i][j] = "X"
            except:
                print("\t\tNot enough characters in diagonal (Topleft to Bottomright)")
                data_matrix[i][j] = "X"


print(xmas_count)
