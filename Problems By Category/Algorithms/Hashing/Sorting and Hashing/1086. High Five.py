def highFive(items):
    scores_by_student = {}
    for student_id, score in items:
        
        if student_id not in scores_by_student:
            scores_by_student[student_id] = []
        scores_by_student[student_id].append(score)

    result = []

    for student_id in sorted(scores_by_student):  
        
        top_five = sorted(scores_by_student[student_id], reverse=True)[:5]
        average = sum(top_five) // 5
        result.append([student_id, average])

    return result



