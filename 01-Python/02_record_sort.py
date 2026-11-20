def sort_key(student):
    name, score = student
    return -score, name

def rank_students(students):
    return sorted(students, key=sort_key)
