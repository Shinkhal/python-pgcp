import csv
import json


def process_student_records(input_csv_path, output_json_path):

    students = []
    with open(input_csv_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["score"] = float(row["score"])
            students.append(row)
    total_students = len(students)
    if total_students > 0:
        average_score = round(
            sum(student["score"] for student in students) / total_students,
            2
        )
    else:
        average_score = 0.0

    if students:
        top = max(students, key=lambda student: student["score"])

        top_scorer = {
            "name": top["name"],
            "score": top["score"]
        }
    else:
        top_scorer = None

    course_counts = {}

    for student in students:
        course = student["course"]
        course_counts[course] = course_counts.get(course, 0) + 1

    summary = {
        "total_students": total_students,
        "average_score": average_score,
        "top_scorer": top_scorer,
        "course_counts": course_counts
    }

    with open(output_json_path, "w", encoding="utf-8") as file:
        json.dump(summary, file, indent=4)
