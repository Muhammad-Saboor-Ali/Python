
# For Loop
print(" For Loop Example")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Using range() to loop through numbers
print("\nNumbers from 0 to 4:")
for i in range(5):  # 0,1,2,3,4
    print(i)


# 2. WHILE LOOP

print("\n2. While Loop Example")
count = 0
while count < 5:
    print("Count is:", count)
    count += 1  # increment to avoid infinite loop

# 3. NESTED LOOPS

print("\n3. Nested Loop Example")
for i in range(1, 4):  # outer loop
    for j in range(1, 4):  # inner loop
        print(f"i = {i}, j = {j}")

# 4. BREAK & CONTINUE

print("\n4. Break and Continue Example")
for number in range(1, 6):
    if number == 3:
        print("Skipping number 3")
        continue  # skip the rest of this iteration
    if number == 5:
        print("Stopping loop at 5")
        break  # exit loop
    print(number)

# 5. ELSE WITH LOOPS

print("\n5. For-Else Example")
for n in range(3):
    print(n)
else:
    print("Loop completed without break!")

