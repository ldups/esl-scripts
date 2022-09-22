first_file = open('output_path_file.txt', 'r')
second_file = open('output_path_file_level_1_test.txt')
first_content = first_file.read().splitlines()
first_hearing = first_content[9]
second_content = second_file.read().splitlines()
second_hearing = second_content[22]
first_hearing = first_hearing.split(',')
second_hearing = second_hearing.split(',')
print('first length: ' + str(len(first_hearing)))
print('second length: ' + str(len(second_hearing)))
difference = list(set(first_hearing).difference(second_hearing))
for path in difference:
    print((path.rsplit('_', 2))[1]) 