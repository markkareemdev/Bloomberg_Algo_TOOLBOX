def meetingRoomii(meetings):
    startTimes = [i[0] for i in meetings]
    endTimes = [i[1] for i in meetings]
    startTimes.sort(reverse=True)
    endTimes.sort(reverse=True)

    rooms = 0
    while len(startTimes)>0:
        startTime = startTimes.pop()

        endTime = endTimes[-1]
        if endTime <= startTime:
            endTime.pop()
        else:
            rooms += 1
    return rooms
