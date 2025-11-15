def calculate_average(grades):
    """Recebe uma lista de notas e retorna a média."""
    return sum(grades) / len(grades)


def get_student_data():
    """Coleta nome e 3 notas do aluno e retorna (nome, média)."""
    name = input("\nStudent name: ")
    n1 = float(input("Grade 1: "))
    n2 = float(input("Grade 2: "))
    n3 = float(input("Grade 3: "))

    average = calculate_average([n1, n2, n3])
    return (name, average)


def show_final_report(students):
    """Exibe o relatório completo da turma."""
    print("\n=== Final Report ===")

    for name, avg in students:
        print(f"{name}: {avg:.2f}")

    class_average = sum(avg for _, avg in students) / len(students)
    print(f"\nClass average: {class_average:.2f}")

    best = max(students, key=lambda x: x[1])
    worst = min(students, key=lambda x: x[1])

    print(f"\nBest student: {best[0]} ({best[1]:.2f})")
    print(f"Worst student: {worst[0]} ({worst[1]:.2f})")


def main():
    """Loop principal do programa."""
    students = []

    while True:
        student = get_student_data()
        students.append(student)
        print(f"Average for {student[0]}: {student[1]:.2f}")

        option = input("\nType 'exit' to stop or press Enter to continue: ")
        if option.lower() == "exit":
            break

    show_final_report(students)


if __name__ == "__main__":
    main()
