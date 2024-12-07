



def check_if_safe(level: list) -> bool:
    is_decreasing = level[0] > level[1]

    for i in range( len(level)-1):

        if abs(level[i] - level[i+1]) > 3 or level[i] == level[i+1] :
            return False
        if is_decreasing and level[i] <= level[i+1] :
            return False
        if not is_decreasing and level[i] > level[i+1]:
            return False
    return True

def main() -> None:
    input = read_input("input.txt")
    
    safe_input = [check_if_safe(x) for x in input]
    print(sum(safe_input))


main()