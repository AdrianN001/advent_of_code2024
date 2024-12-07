

def read_input(file_name: str) -> list[list]:
    with open(file_name, "r") as file:
        raw_input = file.read()
        lines = raw_input.split("\n")
        numbers = [[int(y) for y in x.split(" ")] for x in lines]
        return numbers

def check_if_safe(level: list) -> bool:
    is_decreasing = level[0] > level[1]
    has_failed = False
    for i in range( len(level)-1):

        if abs(level[i] - level[i+1]) > 3 or level[i] == level[i+1] :
            if has_failed:
                return False
            has_failed = True
        elif is_decreasing and level[i] <= level[i+1] :
            if has_failed:
                return False
            has_failed = True
        elif not is_decreasing and level[i] > level[i+1]:
            if has_failed:
                return False
            has_failed = True
    return True

def main() -> None:
    input = read_input("input.txt")
    
    safe_input = [check_if_safe(x) for x in input]
    print(sum(safe_input))


main()