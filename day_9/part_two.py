from itertools import groupby

def read_input(file_name: str) -> list:
    with open(file_name, "r") as file:
        raw_input = file.read()
        return [int(x) for x in raw_input]


def draw_disk(disk: list[str]) -> str: 
    result = []

    curr_block = 0
    for indx, n in enumerate(disk): 
        
        is_block = (indx % 2 == 0)
        if not is_block:
            result.extend(['.']* n)
        else:
            result.extend([f'{curr_block}'] * n)
            curr_block += 1
    
    return result

def move_disk(extended_disk: list[str]) -> list[str]:
    groups = ([list(j) for i, j in groupby(extended_disk)])

    

    print(groups)

def checksum(disk: list[str]) -> int:
    res = 0

    for index, char in enumerate(disk):
        if char == ".": continue
        res += int(char) * (index)
    return res

def main() -> None: 
    input = read_input("test.txt")
    disk = draw_disk(input)
    move_disk(disk)
    print("".join(disk))
    print(checksum(disk))


main()