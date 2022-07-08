# created dictionary
dictionary_of_employees = {"Sanaz": 10000, "Evadne": 20000, "Dipa": 15000, "Hadi": 36000, "Ferdinand": 42000,
                      "Yamileth": 28000, "Marco": 100000, "Ahoth": 12500, "Hari": 11300, "Lughaidh": 50000}

# user input for a name 
name = input("write the name of the employee that you wish to know the salary: ")


salary = str(dictionary_of_employees[name])

print("The salary is £" + salary)
