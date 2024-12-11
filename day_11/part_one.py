import math 

def read_input(file_name: str) -> list:
    with open(file_name, "r") as file:
        raw_input = file.read()
        return [int(num) for num in raw_input.split()]
    

def blink(rocks: list[int]) -> list[int]:
    result = []

    for indx in range(len(rocks)):
        curr = rocks[indx]

        if curr == 0: result.append(1)
        elif (math.floor(math.log10(curr) + 1)) % 2 == 0: 
            str_curr = str(curr)
            left, right = int(str_curr[: len(str_curr) // 2]), int(str_curr[len(str_curr) // 2:])
            result.extend((left, right))
        else:
            result.append(curr * 2024)
    return result, len(result)


def main() -> None:
    input = read_input("input.txt")
    
    for i in range(25): 
        input, length = blink(input)
        print(f"{i+1}. iter = {length}")

main()