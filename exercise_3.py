# created set
set_of_employees = {"Sanaz", "Evadne", "Dipa", "Hadi", "Ferdinand",
                      "Yamileth", "Marco", "Ahoth", "Hari", "Lughaidh"}

award_winners = {"Marco", "Carin", "Antonius"}

# intersection() finds all the values that are the same in both sets
comp_dep_award_winners = award_winners.intersection(set_of_employees)

print("Award winner for the compter department is",comp_dep_award_winners)

# difference removes all the names that are also in award_winners
non_award_winners = set_of_employees.difference(award_winners)

print("The non award winners in the computer department are", non_award_winners)
