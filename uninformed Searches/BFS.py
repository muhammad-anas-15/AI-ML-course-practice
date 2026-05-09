"""
=============================================================================
BREADTH-FIRST SEARCH (BFS) - Complete Implementation
=============================================================================
Author: For FAST NUCES AI Lab
Purpose: Find the SHORTEST path from start to goal

HOW BFS WORKS (Simple Explanation):
1. Start at the beginning
2. Visit ALL neighbors first (level 1)
3. Then visit neighbors of neighbors (level 2)
4. Keep going level by level until you find the goal

IMPORTANT FACTS:
- Uses a QUEUE (First In, First Out)
- ALWAYS finds shortest path (in terms of steps)
- Uses MORE memory than DFS

REAL WORLD USES:
- Finding shortest route on a map
- Social network "degrees of separation"
- Web crawlers
- Puzzle solving (like 8-puzzle)
=============================================================================
"""

from collections import deque  # deque is a fast queue in Python

def bfs(graph, start, goal):
    """
    Find the shortest path from start to goal using BFS.
    
    Parameters:
        graph: A dictionary where each key is a node and 
               the value is a list of connected nodes (neighbors)
        start: The starting node
        goal: The node we want to reach
    
    Returns:
        The path as a list of nodes, or None if no path exists
    
    Example:
        graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
        bfs(graph, 'A', 'D')  # Returns ['A', 'B', 'D'] or ['A', 'C', 'D']
    """
    
    # ============ STEP 1: Setup ============
    # Create a queue. Each item is (current_node, path_to_get_here)
    queue = deque()
    queue.append( (start, [start]) )  # Start with initial node
    
    # Keep track of visited nodes so we don't visit twice
    visited = set()
    visited.add(start)
    
    # ============ STEP 2: Main Loop ============
    while len(queue) > 0:  # While there are nodes to explore
        
        # Get the FIRST item from queue (FIFO)
        current_node, path = queue.popleft()
        
        # ============ STEP 3: Goal Check ============
        if current_node == goal:
            return path  # Found it! Return the path
        
        # ============ STEP 4: Explore Neighbors ============
        # Get all neighbors of current node
        neighbors = graph.get(current_node, [])
        
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)  # Mark as visited
                new_path = path + [neighbor]  # Create new path
                queue.append( (neighbor, new_path) )  # Add to queue
    
    # ============ STEP 5: No Path Found ============
    return None


# ==================== TEST THE CODE ====================
if __name__ == "__main__":
    
    # Create a sample graph (like a map of cities)
    graph = {
        'Peshawar': ['Islamabad', 'Mardan'],
        'Islamabad': ['Peshawar', 'Lahore', 'Rawalpindi'],
        'Mardan': ['Peshawar', 'Swabi'],
        'Lahore': ['Islamabad', 'Multan'],
        'Rawalpindi': ['Islamabad'],
        'Swabi': ['Mardan'],
        'Multan': ['Lahore', 'Karachi'],
        'Karachi': ['Multan']
    }
    
    # Find shortest path from Peshawar to Karachi
    start = 'Peshawar'
    goal = 'Karachi'
    
    result = bfs(graph, start, goal)
    
    if result:
        print("✓ Path found!")
        print("  Path:", " → ".join(result))
        print("  Steps:", len(result) - 1)
    else:
        print("✗ No path exists!")
    
    # Expected Output:
    # ✓ Path found!
    #   Path: Peshawar → Islamabad → Lahore → Multan → Karachi
    #   Steps: 4