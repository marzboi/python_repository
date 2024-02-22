with open("./folder/text.txt") as file:
    content = file.read()
    print(content)

with open("my_file.txt", "a") as file:
    file.write("wepa \n")
