def matrixReshape(mat, r, c):
    if not mat: return mat
    if len(mat) * len(mat[0]) != r * c:
        return mat
    ans = [[0 for i in range(c)] for i in range(r)]
    idx = 0
    while idx < r * c:
        ans[idx // c][ idx % c] =  mat[idx // len(mat[0])][idx % len(mat[0])]
        idx += 1
    return ans

print(matrixReshape([[1,2],[3,4]],1,4))