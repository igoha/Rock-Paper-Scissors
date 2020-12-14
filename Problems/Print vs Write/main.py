numbers = str([1234, 5678, 90])
myfile = open("file_with_list.txt", "w")
print(numbers, file = myfile, end = "")
myfile.close()
