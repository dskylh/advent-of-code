def parse(lines):
    numbers = {}
    symbols: list[tuple[int, int]] = []
    for line_number, line in enumerate(lines):
        number = ""
        for i, char in enumerate(line):
            if char.isdigit():
                number += char
            if number != "" and not char.isdigit():
                number_start_index = i - len(number)
                number_end_index = i - 1
                numbers[(number_start_index, number_end_index, line_number)] = int(
                    number
                )
                number = ""
            if char == "*":
                symbols.append((i, line_number))

    return (numbers, symbols)


def part2():
    file = open("./input.txt")
    lines = file.readlines()
    sum = 0
    numbers, symbols = parse(lines)
    for symbol in symbols:
        gear_numbers = []
        for number in numbers.keys():
            number_line = number[2]
            symbol_line_range = range(symbol[1] - 1, symbol[1] + 2)
            symbol_index_range = range(symbol[0] - 1, symbol[0] + 2)
            number_start_index = number[0]
            number_end_index = number[1]
            if number_line in symbol_line_range and (
                number_start_index in symbol_index_range
                or number_end_index in symbol_index_range
            ):
                gear_numbers.append(numbers[number])

        if len(gear_numbers) == 2:
            sum += gear_numbers[0] * gear_numbers[1]

    print(sum)

    file.close()


if __name__ == "__main__":
    part2()
