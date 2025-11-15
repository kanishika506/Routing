n = int(input("Enter number of nodes: "))

print("\nEnter the cost matrix (use 999 for infinity):")
cost = []
for i in range(n):
    row = list(map(int, input().split()))
    cost.append(row)

dist = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        dist[i][j] = cost[i][j]

print("\n~~Iterations~~")
for k in range(n):
    print(f"\nIteration {k+1}:")
    for i in range(n):
        for j in range(n):
            for v in range(n):
                if dist[i][j] > cost[i][v] + dist[v][j]:
                    dist[i][j] = cost[i][v] + dist[v][j]

    
    for i in range(n):
        print("Distance from node", i, ":", dist[i])

print("\n~~Final Distance Vectors~~")
for i in range(n):
    print("Node", i, ":", dist[i])

print("\nShortest paths calculated successfully...")