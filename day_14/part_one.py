import re

def read_input(file_name: str) -> list:
    with open(file_name, "r") as file:
        raw_input = file.read()
        lines = (x for x in raw_input.split('\n'))
        big = []
        for line in lines:
            res = re.findall(r"[-]?\d+,\s*[-]?\d+", line)
            big.append(tuple(tuple(int(y) for y in x.split(",")) for x in res))
        return big



def main() -> None:

    input = read_input("test.txt")
    print(input)
    
main()