def main():
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


if __name__ == "__main__":
    main()
