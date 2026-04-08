from collections import defaultdict
def solution(edges):
    answer = [0 for _ in range(4)]
    edgeDict = defaultdict(list)
    nodes = set()
    incomingEdges = defaultdict(int)

    for edge in edges:
        x, y = edge
        edgeDict[x].append(y)
        incomingEdges[y] += 1    
        
        nodes.add(x)
        nodes.add(y)
    
    primeNode = 0
    for node in nodes:
        if incomingEdges[node] == 0 and len(edgeDict[node]) > 1: 
            primeNode = node
            break
    answer[0] = primeNode     
    
    for node in edgeDict[primeNode]: 
        incomingEdges[node] -= 1

    for node in nodes:
        if incomingEdges[node] == 2:
            answer[3] += 1
        if node != primeNode and incomingEdges[node] == 0: 
            answer[2] += 1
    answer[1] = len(edgeDict[primeNode]) - (answer[2] + answer[3]) 

    return answer

print(solution([[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]))