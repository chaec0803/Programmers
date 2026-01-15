def solution(visible, hidden, k):
    n = len(visible)
    m = len(visible[0])

    ans = 0
    # === DP (bitmask enumeration) ===
    for rowMask in range(1 << n):
        for colMask in range(1 << m):
            val = 0
            # curr 생성 (기존 curr 의미 그대로)
            curr = [[1] * m for _ in range(n)]
            for i in range(n):
                if (rowMask >> i) & 1:
                    for j in range(m):
                        curr[i][j] *= -1
            for j in range(m):
                for i in range(n):
                    if (colMask >> j) & 1:
                        curr[i][j] *= -1
                    val += visible[i][j] if curr[i][j] == 1 else hidden[i][j]

            cost = k * (bin(rowMask).count("1") + bin(colMask).count("1"))
            ans = max(ans, val - cost)

    return ans

result = solution([[1, 2], [3, 4]],	[[5, 6], [7, 8]],	0)
print(result)