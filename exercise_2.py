# created list
list_of_employees = ["Sanaz", "Evadne", "Dipa", "Hadi", "Ferdinand",
                      "Yamileth", "Marco", "Ahoth", "Hari", "Lughaidh"]

# used sorted() to order the names in list_of_employees 
alphabetical_order_emp_list = sorted(list_of_employees)

# list[0:len(list):2] takes every name starting from the second name with
# index 1 up until the last name of index len(list) and selects a name
# every 2 names 
name_every_second_emp = list_of_employees[1:len(list_of_employees):2]


print("List alphabetically:", alphabetical_order_emp_list)
print("Every second name:", name_every_second_emp)
