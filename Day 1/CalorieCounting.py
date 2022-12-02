def main():
    index = 0               # the current index
    calories = [0]          # full list of totalled calories for each elf
    with open('input1.txt', 'r') as text:
        raw = text.read().splitlines()
        for i in raw:
            try:
                calories[index] += int(i)
            except ValueError:  # only runs if the try statement tries to convert an empty string to an int
                calories.append(0)
                index += 1

        calories.sort()
        print(calories[-1])                                 # Part 1
        print(sum(calories[-3:]))   # Part 2


if __name__ == '__main__':
    main()
