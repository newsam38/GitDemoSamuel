def greetuser(username):
    print(f"Hello, {username}! Welcome to the Python course")


greetuser("John")


def calculateaverage(num1, num2, num3):
    average = (num1 + num2 + num3) / 3
    print(f"The average of {num1}, {num2}, and {num3} is {average}")


calculateaverage(10, 20, 30)

file = open('file1.txt')
total_line = 0

line = file.readline()
while line != "":
    total_line += 1
    line = file.readline()

print(f"Total number of lines: {total_line}")
file.close()
