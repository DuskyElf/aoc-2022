FILE_INPUT: str = 'input.txt'
SAMPLE_INPUT: str = 'sample.txt'

def first_puzzle(file_name: str) -> int:
    max_calories: int = 0
    with open(file_name) as file:
        curr_calories: int = 0
        while True:
            line = file.readline()
            if not line:
                break

            if line == '\n':
                curr_calories = 0
            else:
                curr_calories += int(line)
                if curr_calories > max_calories:
                    max_calories = curr_calories

    return max_calories

def update_top_places(curr_value: int, a, b, c):
    if curr_value > c:
        if curr_value > b:
            if curr_value > a:
                c = b
                b = a
                a = curr_value
            else:
                c = b
                b = curr_value
        else: c = curr_value
    return a, b, c

def second_puzzle(file_name: str) -> int:
    top_1_calories: int = 0
    top_2_calories: int = 0
    top_3_calories: int = 0

    with open(file_name) as file:
        curr_calories: int = 0
        while True:
            line = file.readline()
            if not line:
                break

            if line == '\n':
                top_1_calories, top_2_calories, top_3_calories = update_top_places(curr_calories, top_1_calories, top_2_calories, top_3_calories)
                curr_calories = 0
            else:
                curr_calories += int(line)

        top_1_calories, top_2_calories, top_3_calories = update_top_places(curr_calories, top_1_calories, top_2_calories, top_3_calories)

    return top_1_calories + top_2_calories + top_3_calories

def main():
    print(second_puzzle(FILE_INPUT))

if __name__ == "__main__":
    main()
