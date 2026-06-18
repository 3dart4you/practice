# numbers = [1, 2, 3]
# new_list = [n + 1 for n in numbers]
# print(new_list)

# name = 'Angela'
# new_list = [letter for letter in name]
# print(new_list)
###############################################
# new_list = []
# for n in range(1, 5):
#     new = n * 2
#     new_list.append(new)
# print(new_list)
#
# list = [n * 2 for n in range(1, 5)]
# print(list)
###############################################
# names = ['Alice', 'Bob', 'Charlie', 'Angela', 'Mark', 'Alex', 'Olexii']
# new_list = []
# for name in names:
#     if len(name) <= 4:
#         new_list.append(name)
# print(new_list)
#
# list = [name.upper() for name in names if len(name) <= 4]
# print(list)
###############################################
# import random
# names = ['Alice', 'Bob', 'Charlie', 'Angela', 'Mark', 'Alex', 'Olexii']
# #звичайний підхід
# new_dict = {}
# for s in names:
#     new_dict[s] = random.randint(60, 100)
# print(new_dict)
# #інший підхід
# students = {student:random.randint(60,100) for student in names}
# print(students)
# #перебір через словник
# #звичайний підхід
# passed_students = {}
# for student, score in students.items():
#     if score >= 75:
#         passed_students[student] = score
# print(passed_students)
# #інший підхід
# passed_students = {student:score for (student, score) in students.items() if score >= 75}
# print(passed_students)
###########################################################
import pandas

student_dict = {
    'student': ['Angela', 'James', 'Lily'],
    'score': [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

for index, row in student_data_frame.iterrows():
    if row.student == 'Angela':
        print(row.score)