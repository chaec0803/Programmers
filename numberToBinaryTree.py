def solution(numbers):
    answer = []

    def is_valid(tree):
        # tree는 길이가 (2^k - 1)인 inorder 문자열
        if len(tree) == 1:
            return True

        mid = len(tree) // 2

        # 루트가 0인데, 서브트리에 1이 있으면 불가능
        if tree[mid] == '0' and '1' in tree:
            return False

        # 좌/우 서브트리 재귀 검사
        return is_valid(tree[:mid]) and is_valid(tree[mid+1:])

    for number in numbers:
        binary = bin(number)[2:]
        n = len(binary)

        # 포화 이진트리 길이로 패딩 
            # (next power of 2 - 1 after n)
        k = 1
        while (1 << k) - 1 < n:
            k += 1
        
        full_len = (1 << k) - 1

        tree = binary.rjust(full_len, '0')

        answer.append(1 if is_valid(tree) else 0)

    return answer

solution([2**10])