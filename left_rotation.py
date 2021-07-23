# problem overview : https://www.hackerrank.com/challenges/array-left-rotation/problem
def rotateLeft(d, arr):
    # Write your code here
    result = []
    num = len(arr)
    ed_pt = d% num
    result.extend(arr[ed_pt::])
    result.extend(arr[0:ed_pt])
    return result



arr = [1,2,3,4,5]
d = 4
print(rotateLeft(d, arr))
