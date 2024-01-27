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
