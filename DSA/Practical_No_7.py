def find(parent, i):
    if parent[i] == i:
        return i 
         
    return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskal(graph):
    result = []
    parent = {}
    rank = {}

    for node in graph:
        parent[node] = node
        rank[node] = 0

    edges = []
    for node in graph:
        for neighbor, weight in graph[node]:
            edges.append((weight, node, neighbor))

    edges.sort()

    for edge in edges:
        weight, node1, node2 = edge
        root1 = find(parent, node1)
        root2 = find(parent, node2)
        if root1 != root2:
            result.append(edge)
            union(parent, rank, root1, root2)

    return result

graph = {
    'pune': [('nashik', 5), ('mumbai', 4)],
    'nashik': [('pune', 5), ('mumbai', 7), ('kolhapur', 3)],
    'mumbai': [('pune', 4), ('nashik', 7), ('kolhapur', 5)],
    'kolhapur': [('nashik', 3), ('mumbai', 5)]
}
tree = kruskal(graph)
cost = 0
for i in tree:
  sum =i[0]
  cost = cost + sum

print("The minimum spanning tree :",tree)
#cost = sum(weight for node, neighbor, weight in tree)
print("The cost of minimum spanning tree :”,cost)
