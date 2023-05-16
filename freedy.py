def printjobschedule(array, t):

    m = len(array)
    SortedA = sorted(array, key=lambda x: x[2], reverse=True)

    res = [False] * t
    job = ['-1'] * t

    for q in range(len(SortedA)):
        for q in range(min(t - 1, SortedA[q][1] - 1), -1, -1):
            if res[q] is False:
                res[q] = True
                job[q] = SortedA[q][0]
                break

    print(job)


array = [['a', 7, 202],
         ['b', 5, 29],
         ['c', 6, 84],
         ['d', 1, 75],
         ['e', 2, 43]]

print("Maximum profit sequence of jobs is- ")
printjobschedule(array, 3)

# TC : O(n^2) where,n is no of jobs
