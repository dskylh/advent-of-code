def part2():
    with open("input.txt", "r") as fp:
        lines = fp.readlines()
        ans = 0
        for line in lines:
            digits = []
            for i, c in enumerate(line):
                if c.isdigit():
                    digits.append(c)
                for d, val in enumerate(
                    [
                        "one",
                        "two",
                        "three",
                        "four",
                        "five",
                        "six",
                        "seven",
                        "eight",
                        "nine",
                    ]
                ):
                    if line[i:].startswith(val):
                        digits.append(str(d + 1))
            score = int(digits[0] + digits[-1])
            ans += score
        print(ans)


if __name__ == "__main__":
    part2()
