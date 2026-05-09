"""
=============================================================================
UNIFORM COST SEARCH (UCS) - Complete Implementation
=============================================================================
Author: For FAST NUCES AI Lab
Purpose: Find the CHEAPEST path (lowest total cost) from start to goal

HOW UCS WORKS (Simple Explanation):
1. Start with cost = 0
2. Always expand the node with LOWEST total cost
3. For each neighbor: new_cost = current_cost + edge_cost
4. Keep track of best cost to each node
5. First time we reach goal = we have cheapest path!

KEY DIFFERENCE FROM BFS:
- BFS: Treats all edges as cost 1 (just counts steps)
- UCS: Each edge can have different cost (finds cheapest path)

REAL WORLD USES:
- Google Maps finding fastest route (cost = time)
- Network routing finding cheapest path (cost = bandwidth usage)
- Game AI finding optimal path (cost = energy used)
=============================================================================
"""

import heapq  # Python's built-in priority queue

import heapq

def ucs(graph, start, goal):

    # ============ STEP 1: Setup ============
    # Priority queue stores (cost, node, path)
    priority_queue = []
    heapq.heappush(priority_queue, (0, start, [start]))

    # Keep track of visited nodes
    visited = set()

    # ============ STEP 2: Main Loop ============
    while len(priority_queue) > 0:

        # Get node with LOWEST cost
        cost, current_node, path = heapq.heappop(priority_queue)

        # Skip if already visited
        if current_node in visited:
            continue

        visited.add(current_node)

        # ============ STEP 3: Goal Check ============
        if current_node == goal:
            return cost, path

        # ============ STEP 4: Explore Neighbors ============
        neighbors = graph.get(current_node, [])

        for neighbor, edge_cost in neighbors:

            if neighbor not in visited:
                new_cost = cost + edge_cost
                new_path = path + [neighbor]

                heapq.heappush(priority_queue, (new_cost, neighbor, new_path))

    # ============ STEP 5: No Path Found ============
    return None, None


# ==================== TEST THE CODE ====================
if __name__ == "__main__":
    
    # Weighted graph: each edge has a cost (travel time in hours)
    # Format: 'City': [(neighbor, cost), ...]
    graph = {
        'Peshawar': [('Islamabad', 2), ('Mardan', 1)],
        'Islamabad': [('Peshawar', 2), ('Lahore', 5), ('Murree', 1)],
        'Mardan': [('Peshawar', 1), ('Swabi', 1)],
        'Swabi': [('Mardan', 1), ('Islamabad', 2)],
        'Lahore': [('Islamabad', 5), ('Multan', 4)],
        'Murree': [('Islamabad', 1)],
        'Multan': [('Lahore', 4), ('Karachi', 8)],
        'Karachi': [('Multan', 8)]
    }
    
    cost, path = ucs(graph, 'Peshawar', 'Karachi')
    
    if path:
        print("✓ Cheapest path found!")
        print("  Path:", " → ".join(path))
        print("  Total cost:", cost, "hours")
    else:
        print("✗ No path exists!")
    
    # Expected Output:
    # ✓ Cheapest path found!
    #   Path: Peshawar → Islamabad → Lahore → Multan → Karachi
    #   Total cost: 19 hours