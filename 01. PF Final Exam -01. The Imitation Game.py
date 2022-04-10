encrypted_message = input()
command = input()

while not command == "Decode":
    command = command.split("|")
    if command[0] == "Move":
        num_letters_to_move = int(command[1])
        new_first_part = encrypted_message[num_letters_to_move:]
        new_second_part = encrypted_message[:num_letters_to_move]
        encrypted_message = new_first_part + new_second_part

    elif command[0] == "Insert":
        index = int(command[1])
        value_to_insert = command[2]
        new_first_part = encrypted_message[:index]
        new_third_part = encrypted_message[index:]
        encrypted_message = new_first_part + value_to_insert + new_third_part

    elif command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        encrypted_message = encrypted_message.replace(substring, replacement)
    command = input()

print(f"The decrypted message is: {encrypted_message}")