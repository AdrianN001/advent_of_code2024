def read_input(file_name: str) -> list:
    with open(file_name, "r") as file:
        raw_input = file.read()
        return [[[x, False] for x in line] for line in raw_input.split("\n")]
    
def create_map(input: list[list[str]]) -> list:
    ...


def main() -> None:
    input = read_input("test.txt")
    create_map(input)

main()