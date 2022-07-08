# created dictionary
dictionary_of_employees = {"Sanaz": 10000, "Evadne": 20000, "Dipa": 15000, "Hadi": 36000, "Ferdinand": 42000,
                      "Yamileth": 28000, "Marco": 100000, "Ahoth": 12500, "Hari": 11300, "Lughaidh": 50000}

# created empty lists to display the new and modified employees and their salaries 
employees = []
upperc_employees = []
salaries = []
bonus_salaries = []


# for loop takes the keys from the dictionary_of_employees and adds them to a new list called employees
for employee in dictionary_of_employees:
    employees.append(employee)

print(employees)

# for loop transforms every name in dictionary_of_employees and uses the method .upper() to uppercase all the names
for employee in dictionary_of_employees:
    upperc_employees.append(employee.upper())


print(upperc_employees)

# for loop takes the key values from dictionary_of_employees and adds them to a new list called salaries
for money in dictionary_of_employees:
    salaries.append(dictionary_of_employees[money])

print(salaries)


# for loop adds 1000 bonus money to every money in dictionary_of_employees
for money in dictionary_of_employees:
    bonus = dictionary_of_employees[money] + 1000
    bonus_salaries.append(bonus)

print(bonus_salaries)
