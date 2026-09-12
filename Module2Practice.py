
# 6.1
secret = int(input("Choose a number between 1-10" ))
guess = int(input(" Choose a number between 1-10" ))



if guess < secret:
    print("Too low")
elif guess > secret:
    print("Too high")
else:
    print("Just right!")

# 6.2
    
small = True
green = True

if small:
    if green:
        print("pea")
    else:
        print("cherry")
else:
    if green:
        print("watermelon")
    else:
        print("pumpkin")
        
# 7.1

for value in [3, 2, 1, 0]:
    print(value)

# 7.2

guess_me = 7
number = 1

while True:
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it!")
        break
    else:
        print("oops")
        break
    number += 1

# 7.3

guess_me = 5

for number in range(10):
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it!")
        break
    else:
        print("oops")
        break