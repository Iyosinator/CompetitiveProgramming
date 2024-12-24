
def badSensor(sensor1,sensor2):
    i = 0 
    n = len(sensor1) -1
    while i < n:
        if sensor1[i] != sensor2[i]:
            break
        i += 1
        while i < n:
            if sensor1[i + 1] != sensor2[i]:
                return 1
            if sensor1[i] != sensor2[i + 1]:
                return 2
            i += 1
    return -1