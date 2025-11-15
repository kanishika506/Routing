n = int(input("Enter number of nodes: "))


print("Enter adjacency matrix (999 = no connection):")
graph = []
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

source = int(input("Enter source node (0 to n-1): "))


distance = [9999] * n     
visited = [0] * n         
distance[source] = 0     


for _ in range(n):
    
    min_node = -1
    min_value = 9999
    for i in range(n):
        if visited[i] == 0 and distance[i] < min_value:
            min_value = distance[i]
            min_node = i

    
    visited[min_node] = 1

    
    for j in range(n):
        if graph[min_node][j] != 999:          # there is a link
            new_dist = distance[min_node] + graph[min_node][j]
            if new_dist < distance[j]:
                distance[j] = new_dist

print("\nSHORTEST DISTANCE FROM NODE", source)
for i in range(n):
    print("Node", i, ":", distance[i])