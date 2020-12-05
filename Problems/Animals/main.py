file_animal = open("animals.txt")
file_new = open("animals_new.txt", "w", encoding='utf-8')
for line in file_animal:
    line = line.replace("\n", " ")
    file_new.write(line)
file_animal.close()
file_new.close()
