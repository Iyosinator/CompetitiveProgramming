def maxapples(weights):
    weights.sort()
    result = 0
    counter = 0
    for weight in weights:
        if weight + result <= 5000:
            result += weight
            counter += 1
        else:
            break
    return counter