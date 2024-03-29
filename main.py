bot_name = "Codus"
birth_year = 2024

print(f"""Hello! My name is {bot_name}.
I was created in {birth_year}.""")

user_name = input("Please, remind me your name.\n")
print(f"What a great name you have, {user_name}!")

print("""Let me guess your age.
Enter remainders of dividing your age by 3, 5 and 7.""")

remainder_3 = int(input())
remainder_5 = int(input())
remainder_7 = int(input())

age = (remainder_3 * 70 + remainder_5 * 21 + remainder_7 * 15) % 105
print(f"Your age is {age}; that's a good time to start programming!")

print("Now I will prove to you that I can count to any number you want.")

number = int(input())

for num in range(number + 1):
    print(f"{num} !")

print("""Let's test your programming knowledge.
Why do we use methods?
1. To repeat a statement multiple times.
2. To decompose a program into several small subroutines.
3. To determine the execution time of a program.
4. To interrupt the execution of a program.""")

correct_answer = False

while not correct_answer:
    answer = int(input())
    if answer == 2:
        print("Congratulations, have a nice day!")
        correct_answer = True
    else:
        print("Please, try again.")
