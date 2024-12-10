input_pairs = [[line.split()[0], line.split()[1]] for line in open("input.txt")]
list_a, list_b = sorted([pair[0] for pair in input_pairs]), sorted([pair[1] for pair in input_pairs])
compare_list = zip(list_a, list_b)
total_distance = 0
for pair in compare_list:
    total_distance += abs(int(pair[1]) - int(pair[0]))
print(total_distance)
