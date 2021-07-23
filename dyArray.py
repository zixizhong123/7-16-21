# Project overview : https://www.hackerrank.com/challenges/dynamic-array/problem
def dynamicArray(n, qs):
    # Declaring the variables required
    arr = []
    queries = []
    lastAnswer = 0
    results = []
    #initializing the array
    for j in range(n):
        arr.append([])
    for i in range(len(qs)):
        q_type = qs[i][0]
        dx = qs[i][1]
        dy = qs[i][2]
        loc = ((dx^lastAnswer)%n)
        if q_type == 1:
            arr[loc].append(dy)
        elif q_type == 2:
            lastAnswer = arr[loc][dy%len(arr[loc])]
            results.append(lastAnswer)

    return results
        


    
