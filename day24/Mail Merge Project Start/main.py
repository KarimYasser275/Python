
Names_List = []
with open("./Input/Names/invited_names.txt") as data:
    Names_List = data.readlines()


print(Names_List)

with open("./Input/Letters/starting_letter.txt") as contents:
    letter = contents.read()

print(letter)

for name in Names_List:
    name = name.strip("\n")
    with open(f"./Output/ReadyToSend/{name}_Letter.txt", mode= "w") as data:
        data.write(letter.replace("[name]" , name))