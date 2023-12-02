def part2():
    input = open("./input.txt", "r")
    lines = input.readlines()
    sum = 0
    # red, green, blue
    for i, line in enumerate(lines):
        red, green, blue = 0, 0, 0
        game = line[line.find(":") + 2 :]
        cubes = game.split("; ")
        for cube in cubes:
            color = cube.split(", ")
            for c in color:
                number = int(c[: c.find(" ")])
                if "red" in c and number:
                    red = max(red, number)
                if "green" in c:
                    green = max(green, number)
                if "blue" in c:
                    blue = max(blue, number)

        sum += red * green * blue
    print(sum)

    input.close()


if __name__ == "__main__":
    part2()
