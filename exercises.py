import data1
import data2
import data3
import exercise_functions

# Task 1
print([t.displayname for t in exercise_functions.exercise1(data1.alice, data1.people)])

# Task 2
print([t.displayname for t in exercise_functions.exercise2(data2.alice, data2.people)])

# Task 3
print(sorted(p.displayname for p in exercise_functions.get_members(data2.c_team)))

# Task 4
print(sorted(p.displayname for p in exercise_functions.get_members_v3(data3.c_team)))
