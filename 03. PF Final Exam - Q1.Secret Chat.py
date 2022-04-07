concealed_message = input()
command = input()

while not command == "Reveal":
    command = command.split(":|:")
    if command[0] == "InsertSpace":
        index = int(command[1])
        first_word = concealed_message[0:index]
        second_word = concealed_message[index:]
        concealed_message = first_word + " " + second_word
        print(concealed_message)

    elif command[0] == "Reverse":
        substring = command[1]
        if substring not in concealed_message:
            print("error")
        else:
            concealed_message = concealed_message.replace(substring, "", 1)
            substring = substring[::-1]
            concealed_message = concealed_message + substring
            print(concealed_message)
    elif command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        concealed_message = concealed_message.replace(substring, replacement)
        print(concealed_message)
    command = input()

print(f"You have a new text message: {concealed_message}")