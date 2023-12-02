def part1():
    red, green, blue = 12, 13, 14
    input = open("./input.txt", "r")
    lines = input.readlines()
    sum = 0
    # red, green, blue
    for i, line in enumerate(lines):
        game_number = i + 1
        game = line[line.find(":") + 2 :]
        cubes = game.split("; ")
        for cube in cubes:
            color = cube.split(", ")
            for c in color:
                if "red" in c and int(c[: c.find(" ")]) > red:
                    game_number = 0
                    continue
                if "green" in c and int(c[: c.find(" ")]) > green:
                    game_number = 0
                    continue
                if "blue" in c and int(c[: c.find(" ")]) > blue:
                    game_number = 0
                    continue
                print(c)

            # print(color)
        sum += game_number
    print(sum)

    input.close()


if __name__ == "__main__":
    part1()
