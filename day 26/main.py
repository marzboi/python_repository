import random
list = [1, 2, 3]

list_two = [n * 2 for n in list]


name = 'marco'

new_name = [letter + '1' for letter in name]

number_list = [n * 2 for n in range(1, 5)]


names = ['Marco', 'Alex', 'Quan', 'Ricardo', 'Pedro']

short_names = [name.upper() for name in names if len(name) > 4]


list_of_strings = ['1', '2']
integets_list = [int(n) for n in list_of_strings]


names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleonor']

students_scores = {student: random.randint(1, 100) for student in names}
print(students_scores)

passing_score = {student: score for (student, score) in students_scores.items() if score > 60}
print(passing_score)
