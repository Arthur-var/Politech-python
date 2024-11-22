# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    csv_file = open(INPUT_FILENAME, "r")
    json_file = open(OUTPUT_FILENAME, "w")

    reader = csv.DictReader(csv_file)
    c = []
    for i in reader:
        c.append(i)  # TODO считать содержимое csv файла

    json.dump(c, json_file, indent=4)
    json_file.close()
    csv_file.close()  # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
