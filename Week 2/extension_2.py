in_file = open("name.txt", "r")
name = in_file.read().strip()
print("Your name is", name)
in_file.close()