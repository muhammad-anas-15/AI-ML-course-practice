"""
=============================================================================
DEPTH-FIRST SEARCH (DFS) - Complete Implementation
=============================================================================
Author: For FAST NUCES AI Lab
Purpose: Find A path from start to goal (not necessarily shortest!)

HOW DFS WORKS (Simple Explanation):
1. Start at the beginning
2. Pick ONE path and go as deep as possible
3. When you hit a dead end, BACKTRACK
4. Try another path from the last junction
5. Repeat until you find the goal

IMPORTANT FACTS:
- Uses a STACK (Last In, First Out)
- Does NOT guarantee shortest path
- Uses LESS memory than BFS

REAL WORLD USES:
- Solving mazes
- Game AI (exploring game trees)
- Detecting cycles in graphs
- Topological sorting
=============================================================================
"""

def dfs(graph, start, goal):
    """
    Find a path from start to goal using DFS.
    
    Parameters:
        graph: A dictionary where each key is a node and 
               the value is a list of connected nodes (neighbors)
        start: The starting node
        goal: The node we want to reach
    
    Returns:
        The path as a list of nodes, or None if no path exists
    
    Example:
        graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
        dfs(graph, 'A', 'D')  # Returns a path like ['A', 'B', 'D']
    """
    
    # ============ STEP 1: Setup ============
    # Create a stack. Each item is (current_node, path_to_get_here)
    stack = []
    stack.append((start, [start]))  # Start with initial node
    
    # Keep track of visited nodes so we don't visit twice
    visited = set()
    visited.add(start)
    
    # ============ STEP 2: Main Loop ============
    while len(stack) > 0:  # While there are nodes to explore
        
        # Get the LAST item from stack (LIFO)
        current_node, path = stack.pop()
        
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
                stack.append((neighbor, new_path))  # Add to stack
    
    # ============ STEP 5: No Path Found ============
    return None


# ==================== BONUS: Recursive DFS ====================
def dfs_recursive(graph, current, goal, visited=None, path=None):
    """
    Find a path from start to goal using Recursive DFS.
    
    Parameters:
        graph: Dictionary of nodes and their neighbors
        current: The current node we are visiting
        goal: The node we want to reach
        visited: Set of visited nodes
        path: List showing the path taken so far
    
    Returns:
        Path list if goal is found, otherwise None
    """

    # ============ STEP 1: First Call Setup ============
    # If this is the first function call
    if visited is None:
        visited = set()

    if path is None:
        path = []

    # ============ STEP 2: Visit Current Node ============
    visited.add(current)          # Mark node as visited
    path = path + [current]       # Add node to path

    # ============ STEP 3: Goal Check ============
    if current == goal:
        return path               # Goal found!

    # ============ STEP 4: Explore Neighbors ============
    neighbors = graph.get(current, [])

    for neighbor in neighbors:
        if neighbor not in visited:

            # Recursive call (go deeper)
            result = dfs_recursive(graph, neighbor, goal, visited, path)

            # If goal found in deeper call
            if result:
                return result

    # ============ STEP 5: Dead End ============
    return None


# ==================== TEST THE CODE ====================
if __name__ == "__main__":
    
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    print("DFS (Iterative):", dfs(graph, 'A', 'F'))
    print("DFS (Recursive):", dfs_recursive(graph, 'A', 'F'))
    
    # Note: DFS might find A → B → E → F
    # But shortest path is A → C → F (only 2 steps!)
    # This shows DFS doesn't guarantee shortest path.