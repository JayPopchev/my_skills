import random

def subtract(number_1 , number_2):
    return abs(number_1 - number_2)

def addition(number_1 , number_2):
    return number_1 + number_2

def multiplication(number_1 , number_2):
    return number_1 * number_2

def division(number_1 , number_2):
    while number_2 == 0:
        print("You can't divide by 0, try a new number!")
        number_2 = int(input())
    return number_1 / number_2

def power(number_1 , number_2):
    return number_1 ** number_2

positive_words_list = ["good", "nice", "perfect", "great", "awesome"]
negative_words_list = ["bad", "terrible", "awful", "horrible", "boring"]

print("Choose a data type to perform operations on:")
print("1. Strings")
print("2. Numbers")
print("3. Booleans")
print("4. Additional Data Types (List, Tuple, Dictionary)")

choice = input("Enter the number of your choice (1-4): ")

if choice == '1':
    print(f"Please write a sentence that was a negative word from the list: {negative_words_list}!")
    string_input = input()
    uppercase_string = string_input.upper()
    print(uppercase_string)

    list_string = string_input.split()
    for word in list_string:
        if word in negative_words_list:
            print(f"Why so negative: {word}, let me replace it!")
            index = list_string.index(word)
            list_string.pop(index)
            word = random.choice(positive_words_list)
            list_string.insert(index, word)
            print(" ".join(list_string))

elif choice == '2':
    print("Please choose two integers:")
    number_one = int(input())
    number_two = int(input())

    print(f"Addition result: {addition(number_one, number_two)}")
    print(f"Subtraction result: {subtract(number_one, number_two)}")
    print(f"Multiplication result: {multiplication(number_one, number_two)}")
    print(f"Division result: {division(number_one, number_two)}")
    print(f"Power result: {power(number_one, number_two)}")

elif choice == '3':
    codding_on_python = True
    is_sunny = True

    if is_sunny:
        print("Go play outside!")
        codding_on_python = False

    print("It's starting to rain!")
    bad_weather = True

    if bad_weather:
        print("Go inside and code!")
        codding_on_python = True
        is_sunny = False

    print(f"Is it sunny?: {is_sunny}")
    print(f"Time to code?: {codding_on_python}")

    print("Please select two numbers!")
    num_one = int(input())
    num_two = int(input())

    print(f"{num_one} > {num_two}: {num_one > num_two}")
    print(f"{num_one} < {num_two}: {num_one < num_two}")
    print(f"{num_one} == {num_two}: {num_one == num_two}")

elif choice == '4':
# List Operations
    list_data = [2, 1.5, "hello", True, {"Person": "Name"}]
    list_data.append("Python")
    print(list_data)
    if list_data[3]:
        print(list_data[4])

#Tuple Operations
    fruits = ("Mango", "Apple", "Strawberry", "Banana")
    print(len(fruits))
    for fruit in fruits:
        if fruit == "Apple":
            fruits_list = list(fruits)
            fruits_list[1] = "Kiwi"
            fruits = tuple(fruits_list)
    print(fruits)
#Dictionary Operations
    student_data = {
        "Ivan": {"Math": "6", "English": "5"},
        "Maria": {"Math": "8", "English": "7"},
        "John": {"Math": "9", "English": "6"}
    }

    x = student_data["Ivan"]
    print(x)
    student_data["Peter"] = {"Math": "9", "English": "9"}
    print(student_data)

    print("Maria's Math grade:", student_data["Maria"]["Math"])

    for student, grades in student_data.items():
        print(f"{student}: {grades['Math']}")

else:
    print("Error")
