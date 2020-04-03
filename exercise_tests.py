import unittest

import exercise_functions


class TestExerciseFunctions(unittest.TestCase):

    # Test for task 1
    def test_exercise_1(self):
        from data1 import people, alice
        return_list = exercise_functions.exercise1(alice, people)
        self.assertEqual(['The A-Team', 'The C-Team'], [t.displayname for t in return_list])

    # Test for task 2
    def test_exercise_2(self):
        from data2 import people, alice
        return_list = exercise_functions.exercise2(alice, people)
        self.assertEqual(['The A-Team', 'The C-Team'], [t.displayname for t in return_list])

    # Test for task 3
    def test_exercise_3(self):
        import data2
        self.assertEqual(['Alice', 'Bob', 'Carlos', 'Charlie', 'Eve'],
                         sorted([p.displayname for p in exercise_functions.get_members(data2.c_team)]))

    # Test for task 4
    def test_exercise_4(self):
        import data3
        self.assertEqual(['Alice', 'Bob', 'Carlos', 'Charlie', 'Eve', 'Peggy', 'Trent', 'Victor'],
                         sorted([p.displayname for p in exercise_functions.get_members_v3(data3.c_team)]))


if __name__ == '__main__':
    unittest.main()
