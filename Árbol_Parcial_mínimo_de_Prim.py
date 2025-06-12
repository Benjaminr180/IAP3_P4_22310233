import heapq

# Grafo representado como matriz de adyacencia
graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 1},
    'C': {'A': 3, 'B': 1, 'D': 4, 'E': 5},
    'D': {'B': 1, 'C': 4, 'E': 1},
    'E': {'C': 5, 'D': 1}
}

def prim(graph, start):
    visited = set()
    min_heap = [(0, start, None)]  # (peso, nodo, nodo_origen)
    total_cost = 0
    mst = []

    print(f"\nInicio desde el nodo: {start}")
    while min_heap:
        cost, current, origin = heapq.heappop(min_heap)
        if current in visited:
            continue

        visited.add(current)
        if origin:
            mst.append((origin, current, cost))
            total_cost += cost
            print(f"Seleccionado: ({origin} -> {current}) con peso {cost}")
        
        for neighbor, weight in graph[current].items():
            if neighbor not in visited:
                heapq.heappush(min_heap, (weight, neighbor, current))

        print(f"Nodos visitados: {visited}")
        print("-" * 40)

    print("\nÁrbol de Expansión Mínima construido:")
    for edge in mst:
        print(f"{edge[0]} -- {edge[2]} --> {edge[1]}")
    print(f"\nCosto total: {total_cost}")

# Ejecutar algoritmo de Prim desde nodo A
prim(graph, 'A')
