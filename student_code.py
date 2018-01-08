def shortest_path(M,start,goal):
    # Initialize list and other variables
    frontier = set()
    explored = []
    parent = {}
    point_gcost = {}
    point_hcost = {}
    point_fcost = {}
    
    # Initialise current
    current = start
    frontier.add(current)
    point_gcost[current] = 0
    point_fcost[current] = 2
    parent[current] = None
 
    while frontier:
                
        if current == goal:
            path = []
            while parent[current]:
                path.append(current)
                current = parent[current]
            path.append(current)
            return path[::-1]
        
        frontier.remove(current)  # remove best item
        explored.append(current)  # add new
        
        for node in M.roads[current]:
            if node in explored:
                continue
            if node in frontier:
                new_gcost = point_gcost[current] + gcost(M, node, current)
                if point_gcost[node] > new_gcost:
                    point_gcost[node] = new_gcost
                    parent[node] = current
                break
            else:
                point_gcost[node] = point_gcost[current] + gcost(M, node, current)
                point_hcost[node] = hcost(M, node, goal)
                parent[node] = current
                frontier.add(node)
                
        # find minimum, update current
        minimum = None
        for node in frontier:
            point_fcost[node] = point_gcost[node] + point_hcost[node]
            
            if minimum is None or point_fcost[node] < point_fcost[minimum]:
                minimum = node
                
        current = minimum

def gcost(M, node1, node2):
    nodeone = M.intersections[node1]
    nodetwo = M.intersections[node2]
    a = abs(nodeone[0] - nodetwo[0]) 
    b = abs(nodeone[1] - nodetwo[1]) 
    g_cost = a + b
    return g_cost
                    
def hcost(M, node, goal):
    nodetwo = M.intersections[goal]
    nodeone = M.intersections[node]
    x = abs(nodeone[0] - nodetwo[0])
    y = abs(nodeone[1] - nodetwo[1])
    h_cost = x + y
    return h_cost
