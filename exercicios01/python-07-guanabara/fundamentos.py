from time import sleep

number = input("write an integer: ")
number = int(number)
print("This is number predecessor {} successor {}".format(number - 1, number + 1))

print('PROCESSANDO...')

sleep(2)

salary = input("what's your salary: ")
try:
    salary = float(salary)
    print(f"Your salary: {salary}")
except ValueError:
    print("Please enter a valid number for the salary.")
