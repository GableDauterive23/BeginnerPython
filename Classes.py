class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 30000)
emp_3 = Employee('John', 'Hi', '30')

print(emp_2.email)
print(emp_1.email)
print(emp_3.email + ' ' + emp_3.first)
