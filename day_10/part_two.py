def read_input(file_name: str) -> list:
    with open(file_name, "r") as file:
        raw_input = file.read()
        return [[int(x) for x in line] for line in raw_input.split("\n")]
    

paths = []

def search_path(map: list[list], prev_indx: list[tuple], curr_indx: tuple) -> None:
    global paths
    
    y, x = curr_indx
    current_value = map[y][x]
    if current_value == 9:
        paths.append(prev_indx)

    top = bottom = left = right = float('-inf')
    
    if y != 0:              top = map[y-1][x]

    if y != len(map)-1:     bottom = map[y+1][x]

    if x != 0:              left = map[y][x-1]

    if x != len(map[x]) -1: right = map[y][x+1]

    if (top-1) == current_value: search_path(map, [*prev_indx, (y-1, x)], (y-1, x))
    if (bottom-1) == current_value: search_path(map, [*prev_indx, (y+1, x)], (y+1, x))
    if (left-1) == current_value: search_path(map, [*prev_indx, (y, x-1)], (y, x-1))
    if (right-1) == current_value: search_path(map, [*prev_indx, (y, x+1)], (y, x+1))

def solve(map: list[list]) -> int:
    global paths

    for y in range(len(map)):
        row = map[y]
        for x in range(len(row)):
            current_index = (y, x)

            if row[x] == 0:
                search_path(map, [current_index], current_index)

    paths = [(path[0], path[-1]) for path in paths]
    
    return len(paths)


def main() -> None: 
    input = read_input("input.txt")
    result = solve(input)
    print(result)


main()