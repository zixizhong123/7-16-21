# Project overview : https://www.hackerrank.com/challenges/2d-array/problem
def hourglassSum(arr):
    # Write your code here
    sums = []
    for i in range(len(arr)-2): # traveling lines
        for j in range(4): #traveling elements in each line
            temp = []
            temp+=arr[i][j:j+3]
            temp+=[arr[i+1][j+1]]
            temp+=arr[i+2][j:j+3]
            sums.append(sum(temp))
            #this line is for debugging, it will print out temp for every iteration
            # print(temp) 

    return max(sums)
