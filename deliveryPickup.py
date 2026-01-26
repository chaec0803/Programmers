def solution(cap, n, deliveries, pickups):
    answer = 0
    deliverySum = 0
    pickupSum = 0

    for i in range(n - 1, -1, -1):
        deliverySum += deliveries[i]
        pickupSum += pickups[i]
        # if package is left after delivery / pickup, 
            # use trips to deliver / pick up package to / from house i 

        # negative deliverySum or pickupSum = space is left on truck
            # don't use trips here
        cnt = 0
        while deliverySum > 0 or pickupSum > 0:
            deliverySum -= cap
            pickupSum -= cap
            cnt += 1

        answer += (i + 1) * 2 * cnt

    return answer

print(solution(4,	5,	[1, 0, 3, 1, 2],	[0, 3, 0, 12, 0]))