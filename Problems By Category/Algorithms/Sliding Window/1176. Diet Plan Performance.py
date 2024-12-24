def dietPlanPerformance(calories,k,lower,upper):
    points = 0
    current_sum = sum(calories[:k])
    
    if current_sum < lower:
        points -= 1
    elif current_sum > upper:
        points += 1

    for i in range(k,len(calories)):
        current_sum += calories[i] - calories[i-k]
        if current_sum < lower:
            points -=1
        elif current_sum > upper:
            points +=1
    return  points

    