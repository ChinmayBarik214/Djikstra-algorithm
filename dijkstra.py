def dijkstra(graph, src, dest):
    inf = float('inf')
    node_data = {
    'A': {'distance': inf, 'prev':[]},
    'B': {'distance': inf, 'prev': []},
    'C': {'distance': inf, 'prev': []},
    'D': {'distance': inf, 'prev': []},
    'E': {'distance': inf, 'prev': []}
    }
    node_data[src]['distance'] = 0
    visited = []
    unvisited = ['A', 'B', 'C', 'D', 'E']
    current_node = src
    while unvisited:
        if current_node not in visited:
            visited.append(current_node)
            unvisited.remove(current_node)
            neighbor = []
            for j in graph[current_node]:
                if j not in visited:
                    distance = node_data[current_node]['distance'] + graph[current_node][j]
                    if distance < node_data[j]['distance']:
                        node_data[j]['distance'] = distance
                        node_data[j]['prev'] = node_data[current_node]['prev'] + [current_node]
                    neighbor.append((node_data[j]['distance'], j))
        try:
            current_node = min(neighbor)[1]
        except:
            continue
    print("Shortest Distance:", node_data[dest]['distance'])
    print("Shortest Path:", node_data[dest]['prev'] + list(dest))

if __name__ == "__main__":
    graph = {
    'A': {'B': 6, 'D': 1},
    'B': {'A': 6, 'C': 5, 'D': 2, 'E': 2},
    'C': {'B': 5, 'E': 5},
    'D': {'A': 1, 'B': 2, 'E': 1},
    'E': {'D': 1, 'B': 2, 'C': 5},
    }
    source = 'A'
    destination = 'C'
    
    dijkstra(graph, source, destination)
