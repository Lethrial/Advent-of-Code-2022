def main():
    index = 0       # the current index
    calories = [0]  # full list of totalled calories for each elf
    largest = 0     # the current largest number
    with open('input1.txt', 'r') as text:
        raw = text.read().splitlines()
        for i in raw:
            try:
                calories[index] += int(i)
            except ValueError:  # only runs if the try statement tries to convert an empty string to an int
                if calories[index] > largest:
                    largest = calories[index]
                calories.append(0)
                index += 1
        print(largest)


if __name__ == '__main__':
    main()
