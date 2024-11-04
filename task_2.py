# TODO Напишите функцию find_common_participants
def find_common_participants(first_command, second_command, delimiter=','):
    set_first_command = set(first_command.split(delimiter))
    set_second_command = set(second_command.split(delimiter))
    intersection_command = set_second_command.intersection(set_first_command)
    return sorted(intersection_command)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group, delimiter='|'))
# TODO Провеьте работу функции с разделителем отличным от запятой
