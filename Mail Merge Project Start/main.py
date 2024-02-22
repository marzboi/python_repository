list_of_names = []

with open('./Input/Names/invited_names.txt', 'r') as file:
    list_of_names_raw = file.readlines()
    for name in list_of_names_raw:
        clean_name = name.strip("\n")
        list_of_names.append(clean_name)

for name in list_of_names:
    letter_content = []
    with open("./Input/Letters/starting_letter.txt", 'r') as file:
        letter_content = file.readlines()

    letter_content[0] = letter_content[0].replace("[name]", name)
    print(letter_content)

    for line in letter_content:
        with open(f"./Output/ReadyToSend/{name}_letter.txt", "a") as letter:
            letter.write(line)


# PLACEHOLDER = "[name]"


# with open("./Input/Names/invited_names.txt") as names_file:
#     names = names_file.readlines()

# with open("./Input/Letters/starting_letter.txt") as letter_file:
#     letter_contents = letter_file.read()
#     for name in names:
#         stripped_name = name.strip()
#         new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
#         with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
#             completed_letter.write(new_letter)
