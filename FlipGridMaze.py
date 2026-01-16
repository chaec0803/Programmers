def solution(visible, hidden, k):
    n = len(visible)
    m = len(visible[0])

    ans = -10**18

    for rowMask in range(1 << n):
        rowCnt = bin(rowMask).count("1")

        for colMask in range(1 << m):
            colCnt = bin(colMask).count("1")
            cost = k * (rowCnt + colCnt)

            total = 0
            min_odd = 10**18  # (i+j)%2==1 최소값

            for i in range(n):
                rf = (rowMask >> i) & 1
                for j in range(m):
                    flipped = rf ^ ((colMask >> j) & 1)
                    val = hidden[i][j] if flipped else visible[i][j]
                    total += val

                    if (i + j) & 1:
                        min_odd = min(min_odd, val)

            if n % 2 == 0 and m % 2 == 0:
                total -= min_odd

            ans = max(ans, total - cost)

    return ans
