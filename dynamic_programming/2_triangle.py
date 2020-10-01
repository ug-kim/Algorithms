def solution(triangle):
    length = len(triangle)

    for i in range(length-2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] = max(triangle[i][j] + triangle[i+1]
                                 [j], triangle[i][j] + triangle[i+1][j+1])

    return triangle[0][0]
