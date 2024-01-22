import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

students_scores = {student: random.randint(1, 100) for student in names}
# print(students_scores)
# Example: (these values will change everytime you run it) -  {'Alex': 89, 'Beth': 30, 'Caroline': 33, 'Dave': 52, 'Eleanor': 52, 'Freddie': 47}

# 60 or higher, passes:

# Dictionary Comprehension format:
# new_dict = {new_key: new_value for (key, value) in dict.items() if testpasses}  # we call the items() Method on the dictionary file. (it is not just items as an attribute, so add () to make it a Method). You ADD .items() to the end of the dictionary file name.
# passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}   # (This iteration, is it >= 60 THIS iteration?)
# new_dict = {new_key: new_value for (key, value) in dict.items() if testpasses}
passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}    # "in" = what we want to loop through (which is the dictionary)
print(f"Passed student(s): {passed_students}")


'''
passed_students = {
    "Beth": 72
}
'''