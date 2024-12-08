
def read_input(file_name: str) -> list:
    with open(file_name, "r") as file:
        raw_input = file.read()
        lines = raw_input.split("\n")
        parts = [x.split(": ") for x in lines]
        typed_parts = [ (int(val), [int(x) for x in nums.split(" ")]) for val, nums in parts]
        return typed_parts

def can_solve(result: int, numbers: list[int]) -> bool:

    sub_values = []
    x = numbers[0]
    y = numbers[1]
    sub_values.extend([x+y, x*y])

    for i in range(2, len(numbers)):
        sec_operand = numbers[i]

        curr_state = sub_values.copy()
        sub_values.clear()
        for prev_sub_val in curr_state:
            sub_values.extend([prev_sub_val*sec_operand, prev_sub_val+sec_operand])
    return result in sub_values

def main() -> None:
    inputs = read_input("./input.txt")
    result = 0
    for res, numbers in inputs:
        solveable = can_solve(res, numbers)
        result += (solveable * res)
    print(result)

main()