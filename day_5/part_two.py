

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

def correct_update(update: list[int], rules: list[list[int]]) -> list[int]:
   
    found_error = False

    while True:
        for i in range(0, len(update)):

            point_a = update[i]
            for j in range(i, len(update)):
                point_b = update[j]

                for a, b in rules:
                    if a == point_b and b == point_a:
                        found_error = True
                        update.pop(j)
                        update.insert(i, point_b)
        
        if not found_error:
            break
        found_error = False
    return update



def get_middle(update: list[int]) -> int:
    return update[ len(update) // 2] 

def main() -> None:
    rules, updates = read_input("input.txt")
    result = 0

    for update in updates:
        valid = check_if_valid(update, rules)
        if valid: continue
        corrected = correct_update(update, rules)
        result += get_middle(corrected)
    print(result)
main()