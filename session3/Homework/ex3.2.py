import random

word = ['meticulous', 'champion', 'hexagon']
word_random = random.SystemRandom()
n = word_random.choice(word)

char_list = list(n)

random.shuffle(char_list)
m = ''.join(char_list)
for i in m:
    print(i,end=" ")
print()
a = input("Enter your answer: ")
loop = True
while loop:
    if a == n:
        print("Congratulation!")
        loop = False
    else:
        print("Wrong answer")
        a = input("Enter your answer: ")