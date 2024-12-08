


def read_input(file_name: str) -> list[str]:
    with open(file_name, "r") as file:
        raw_input = file.read()
        
        lines = raw_input.split("\n")
        return [[y for y in x] for x in lines]

def try_index(input: list[list], x: int, y: int) -> str:
    if y < 0 or y >= len(input):
        return ''
    row = input[y]
    if x < 0 or x >= len(row):
        return ''
    return row[x]


def get_neighbour_block(input: list[list], x: int, y: int, radius: int) -> list[str]:
    neighbours = []

    for y_offset in range(-radius // 2, radius // 2 + 1):
        row = []
        for x_offset in range(-radius // 2, radius // 2 + 1):
            row.append(try_index(input, x + x_offset, y + y_offset))
        neighbours.append(row)

    return neighbours



def search_xmas(neighbours: list[str]) -> int:
    result = 0

    result += (neighbours[0][0] + neighbours[1][1] + neighbours[2][2] + neighbours[3][3] == "SAMX")
    result += (neighbours[0][3] + neighbours[1][3] + neighbours[2][3] + neighbours[3][3] == "SAMX")
    result += (neighbours[0][6] + neighbours[1][5] + neighbours[2][4] + neighbours[3][3] == "SAMX")

    result += ("".join(neighbours[3][:4]) == "SAMX")
    result += ("".join(neighbours[3][3:]) == "XMAS")

    result += (neighbours[6][6] + neighbours[5][5] + neighbours[4][4] + neighbours[3][3] == "SAMX")
    result += (neighbours[6][3] + neighbours[5][3] + neighbours[4][3] + neighbours[3][3] == "SAMX")
    result += (neighbours[6][0] + neighbours[5][1] + neighbours[4][2] + neighbours[3][3] == "SAMX")

    return result




def main() -> None:
    input = read_input("input.txt")
    width, height = len(input[0]), len(input)
    result = 0
    for y in range(height):
        for x in range(width):
            if input[y][x] == "X":
                neighbours = get_neighbour_block(input, x, y, 6)
                result += search_xmas(neighbours)
    print(result)
main()