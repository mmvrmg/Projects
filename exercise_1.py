# created tuple
tuple_of_employees = ("Sanaz", "Evadne", "Dipa", "Hadi", "Ferdinand",
                      "Yamileth", "Marco", "Ahoth", "Hari", "Lughaidh")

# used len() to find the total number of values inside the tuple "tuple_of_employees"
number_of_employees = len(tuple_of_employees)

# .index() was used to find the position value of the name Marco
my_position = tuple_of_employees.index("Marco")

print("These are the current employees in the computer department \n",
      tuple_of_employees)

print("Number of employees:", number_of_employees)
print("This is your position:", my_position)
