with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()

for name in names:
    name = name.strip()
    revised = letter.replace("[name]", name)

    with open(f"./Output/ReadyToSend/letter_to_{name}", "w") as new_letter:
        new_letter.write(revised)

