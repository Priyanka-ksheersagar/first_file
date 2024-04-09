file_name = input("enter the file name: ")
handle = open(file_name)
for line in handle:
    line_starting_with_a = line.startswith("a")
    print(line_starting_with_a)