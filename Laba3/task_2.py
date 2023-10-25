def find_common_participants(first, second, f=','):
    new = []
    first = first.split(f)
    second = second.split(f)
    for i in first:
        for j in second:
            if i==j:
                new.append(i)
    new.sort()
    return new
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group,'|' ))
