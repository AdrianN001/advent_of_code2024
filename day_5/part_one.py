

def read_input(file_name: str) -> tuple[list, list]:
    with open(file_name, "r") as file:
        raw_input = file.read()
        
        rules, update = raw_input.split("\n\n")
        
        rules = [[int(y) for y in x.split("|")] for x in rules.split("\n")]
        update = [[int(y) for y in x.split(",")] for x in update.split("\n")]
        return rules, update

def check_if_valid(update:list[int], rules:list[list[int]]) -> bool:

    for i in range(0, len(update)):

        start = update[i]
        for j in range(i, len(update)):
            end = update[j]

            for a, b in rules:
                if a == end and b == start:
                    return False
    return True

def get_middle(update: list[int]) -> int:
    return update[ len(update) // 2] 

def main() -> None:
    rules, updates = read_input("input.txt")
    result = 0

    for update in updates:
        valid = check_if_valid(update, rules)
        result += get_middle(update) * valid
    print(result)
main()