from bisect import bisect_left
from itertools import combinations

def solution(dice):
    n = len(dice)
    half = n // 2
    all_idx = set(range(n))

    def get_sums(group):
        sums = [0]
        for idx in group:
            new_sums = []
            for s in sums:
                for val in dice[idx]:
                    new_sums.append(s + val)
            sums = new_sums
        return sums

    best_group = None
    max_wins = -1

    # only generate one side of each complementary pair
    # force 0 to be included
    for comb in combinations(range(1, n), half - 1):
        group_a = (0,) + comb
        group_b = tuple(sorted(all_idx - set(group_a)))

        sums_a = get_sums(group_a)
        sums_b = sorted(get_sums(group_b))

        wins = 0
        for s in sums_a:
            wins += bisect_left(sums_b, s)

        if wins > max_wins:
            max_wins = wins
            best_group = group_a

    return [x + 1 for x in best_group]