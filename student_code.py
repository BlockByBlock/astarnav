import math

def shortest_path(M,start,goal):
    # Initialize list and other variables
    frontier = set()
    explored = set()
    parent = {}
    point_gcost = {}
    point_fcost = {}
    
    # Initialise current
    current = start
    frontier.add(current)
    point_gcost[current] = 0
    point_fcost[current] = point_gcost[current] + cost(M, start, goal)
    parent[current] = None
 
    #while there is possible path in frontier
    while frontier:

        current = min(frontier, key=lambda x:point_fcost[x])
        
        # reach goal, trace path
        if current == goal:
            path = []
            while parent[current]:
                path.insert(0, current)
                current = parent[current]
            path.insert(0, current)
            return path
        
        # reached and tested
        frontier.remove(current)
        explored.add(current)    
        
        # neighbour checks
        for node in M.roads[current]:
            if node in explored:
                continue  # Evaluated
                
            if node not in frontier:
                frontier.add(node)
                point_gcost[node] = point_gcost[current] + cost(M, node, current)
                point_fcost[node] = point_gcost[node] + cost(M, node, goal)
                parent[node] = current
                
            new_gcost = point_gcost[current] + cost(M, node, current)
            
            if point_gcost[node] > new_gcost :
                point_gcost[node] = new_gcost
                point_fcost[node] = point_gcost[node] + cost(M, node, goal)
                parent[node] = current                
                        
def cost(M, node1, node2):
    nodeone = M.intersections[node1]
    nodetwo = M.intersections[node2]
    a = nodeone[0] - nodetwo[0] 
    b = nodeone[1] - nodetwo[1] 
    cost = math.sqrt((a ** 2) + (b ** 2))
    return cost
                    
