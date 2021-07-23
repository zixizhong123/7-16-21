# problem overview: https://www.hackerrank.com/challenges/sparse-arrays/problem
def matchingStrings(strings, queries):
    result = []
    reference = {}
    for s_item in strings:
        if s_item in reference:
            reference[s_item] += 1
        else:
            reference[s_item] = 1
    for q_item in queries:
        if q_item in reference:
            result.append(reference[q_item])
        else:
            result.append(0)
    return result

