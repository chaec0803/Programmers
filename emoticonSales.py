def solution(users, emoticons):
    sales = [10, 20, 30, 40]
    ans = []

    def getResult(curr):
        membership = 0
        emojiPrice = 0
        for user in users:
            rate, limit = user
            price = 0
            for i in range(len(curr)):
                sale = curr[i]
                if sale >= rate: 
                    price += (100 - sale) * 0.01 * emoticons[i]
            if price >= limit: 
                membership += 1
            else:
                emojiPrice += price  

        return [membership, emojiPrice]
                

    def backtrack(curr):
        if len(curr) == len(emoticons):
            ans.append(getResult(curr))
            return

        for s in range(len(sales)):
            curr.append(sales[s])
            backtrack(curr)
            curr.pop()

    backtrack([])

    ans = sorted(ans, key = lambda x: x[1], reverse= True)
    ans = sorted(ans, key = lambda x: x[0], reverse=True)

    return ans[0]

print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))