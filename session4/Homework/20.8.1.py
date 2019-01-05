letter = input("Enter your string: ").lower()
letter_counts = {}
for i in letter:
    letter_counts[i] = letter_counts.get(i, 0) + 1
print(letter_counts)