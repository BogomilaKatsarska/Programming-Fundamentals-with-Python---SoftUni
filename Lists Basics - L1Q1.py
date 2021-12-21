# 1.	Strange Zoo
# You are at the zoo and the meerkats look strange.
# You will receive 3 strings: (tail, body, head).
# Your task is to re-arrange the elements in a list, so that the animal looks normal again: (head, body, tail).


tail = input()
body = input()
head = input()
meerkat = [head, body, tail]

print(meerkat)

#swapping elements(none of the els is lost):
# meerkat = [tail, body, head]
# meerkat[0], meerkat[2] = meerkat[2], meerkat[0]
# print(meerkat)
# meerkat[0] = meerkat [2] -> reassignment