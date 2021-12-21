# You will be given a number n. On the next n lines you will receive integers. You should create and print two lists:
# •	One with all the positives (including 0) numbers
# •	One with all the negatives numbers
# Finally, print the following message: "Count of positives: {count_positives}. Sum of negatives: {sum_of_negatives}"


n = int(input())
positives_list = []
negatives_list = []

for num in range(n):
    num = int(input())
    if num < 0:
        negatives_list.append(num)
    else:
        positives_list.append(num)

print(positives_list)
print(negatives_list)
print(f"Count of positives: {len(positives_list)}")
print(f"Sum of negatives: {sum(negatives_list)}")