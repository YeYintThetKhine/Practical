outFile = open("name.txt", "w")
name = input("What is your name? ")
print(name, file=outFile)  # or outFile.write(name)
outFile.close()
