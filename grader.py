def grade(action, expected):
    if action == expected:
        return 1.0
    elif action == "visit_doctor":
        return 0.5
    else:
        return 0.0
    