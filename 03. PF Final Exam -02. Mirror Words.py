import re

regex = r"(@|#)([a-zA-Z]{3,})(\1)(\1)([a-zA-Z]{3,})(\1)"
text = input()
mirror_words = []

matches = re.finditer(regex, text)
count = 0

for match in matches:
    count += 1
    first_group = match.group(2)

    second_group = match.group(5)
    second_group_reversed = second_group[::-1]

    if first_group == second_group_reversed:
        mirror_words.append(f"{first_group} <=> {second_group}")


if count == 0:
    print(f"No word pairs found!")
else:
    print(f"{count} word pairs found!")

if len(mirror_words) == 0:
    print(f"No mirror words!")
else:
    print(f"The mirror words are:")
    print(", ".join(mirror_words))