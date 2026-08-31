def compile_feedback(ratings_dict):
    compiled = {}

    for course, ratings in feedback_data.items():
        valid = []
        for rating in ratings:
            try:
                valid.append(float(rating))
            except (ValueError, TypeError):
                print(f"Warning: Invalid rating value '{rating}' in course '{course}' skipped.")

        try:
            average = sum(valid)/ len(valid)
        except ZeroDivisionError:
            print(f"Warning: No valid rating found for course {course}"
                  f"Rating set to 0.0"
            )
            average = 0.0
        compiled[course] = round(average, 2)
    return compiled

feedback_data = {
    "Python Programming": [5, 4, "4", "Great", 5],
    "Machine Learning": [],
    "Deep Learning": ["Good", "Average", None]
}

print(compile_feedback(feedback_data))
