def get_grade(score):
    if score >= 80:
        return "Great"
    elif score >= 60:
        return "Pass"
    else:
        return "Fail"

print(get_grade(85))
print(get_grade(70))
print(get_grade(40))