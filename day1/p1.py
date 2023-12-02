def part1():
    with open("input.txt", "r") as fp:
        lines = fp.readlines()
        sum = 0
        for line in lines:
            num1: str
            num2: str
            i = 0
            j = len(line) - 1
            while not line[i].isdigit():
                i += 1
            while not line[j].isdigit():
                j -= 1
            num1 = line[i]
            num2 = line[j]
            sum += int(num1 + num2)
        print(sum)


def part1_alt():
    with open("input.txt", "r") as fp:
        ans = 0
        lines = fp.readlines()
        for line in lines:
            digits = []
            for i, c in enumerate(line):
                if c.isdigit():
                    digits.append(c)
            score = int(digits[0] + digits[-1])
            ans += score
    print(ans)


if __name__ == "__main__":
    part1()
