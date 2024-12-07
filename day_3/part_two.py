import re

def read_input(file_name: str) -> list[str]:
    with open(file_name, "r") as file:
        raw_input = file.read()
        
        return re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", raw_input)
    
def filter_the_input(input: list[str]) -> list[str]:
    res = []
    activated = True

    for i in input:
        if activated and i.startswith("mul"):
            res.append(i)
        elif i.startswith("don't"):
            activated = False
        elif i.startswith("do("):
            activated = True
    return res
            

def evaluate_mul(instruction: str) -> int:
    instruction = instruction.removeprefix("mul(").replace(")","").split(",")
    print(instruction)
    numbers = [int(x) for x in instruction]

    res = 1
    for i in numbers:
        res *= i
    return res

def main() -> None:
    input = read_input("input.txt")
    input = filter_the_input(input)
    
    print(sum([evaluate_mul(x) for x in input]))


main()