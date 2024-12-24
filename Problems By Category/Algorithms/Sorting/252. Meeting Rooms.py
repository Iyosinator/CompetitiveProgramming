def MeetingRooms(intervals):
    intervals.sort(key = lambda x:x[0])
    n = len(intervals)
    for i in range(n-1):
        if intervals[i-1][1] > intervals[i][0]:
            return False
    return True