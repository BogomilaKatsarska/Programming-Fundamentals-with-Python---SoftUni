n = int(input())
piano_pieces = {}

for _ in range(n):
    piece, composer, key = input().split("|")
    piano_pieces[piece] = {"composer": composer, "key": key}

command = input()

while not command == "Stop":
    command = command.split("|")
    if command[0] == "Add":
        piece = command[1]
        composer = command[2]
        key = command[3]

        if piece in piano_pieces:
            print(f"{piece} is already in the collection!")
        else:
            # piano_pieces[piece]["composer"] = composer
            # piano_pieces[piece]["key"] = key
            piano_pieces[piece] = {"composer": composer, "key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif command[0] == "Remove":
        piece = command[1]

        if piece not in piano_pieces:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            print(f"Successfully removed {piece}!")
            piano_pieces.pop(piece)

    elif command[0] == "ChangeKey":
        piece = command[1]
        new_key = command[2]

        if piece not in piano_pieces:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            piano_pieces[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")

    command = input()

for key, value in piano_pieces.items():
    print(
        f"{key} -> Composer: {value['composer']}, Key: {value['key']}")