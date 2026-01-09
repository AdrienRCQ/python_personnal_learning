from dataclasses import dataclass

@dataclass(order=True)
class Student:
    grade: float
    name: str
    age: int

# Création de quelques étudiants
student1 = Student(15.5, "Patrick", 20)
student2 = Student(14.0, "Robert", 21)
student3 = Student(15.5, "Ely", 19)
student4 = Student(9.0, "Damien", 22)

# Maintenant on peut comparer et trier les étudiants
# Par défaut, la comparaison se fait sur tous les champs dans l'ordre de déclaration
print(student1 > student2)  # True (car 15.5 > 14.0)
print(student1 == student3)  # False car les noms sont différents

# On peut aussi trier une liste d'étudiants
students = [student2, student3, student1, student4]
sorted_students = sorted(students)
for student in sorted_students:
    print(f"{student.name}: {student.grade}")


