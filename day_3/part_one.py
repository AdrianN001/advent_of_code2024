import re

def read_input(file_name: str) -> list[str]:
    with open(file_name, "r") as file:
        raw_input = file.read()
        
        return re.findall(r"mul\(\d{1,3},\d{1,3}\)", raw_input)
    
def evaluate_mul(instruction: str) -> int:
    instruction = instruction.removeprefix("mul(").replace(")","").split(",")
    print(instruction)
    numbers = [int(x) for x in instruction]

    res = 1
    for i in numbers:
        res *= i
    return res

def main() -> None:
    input = read_input("test.txt")
    
    print(sum([evaluate_mul(x) for x in input]))


main()