import math

def shortest_path(M,start,goal):
    # Initialize list and other variables
    frontier = set()
    explored = set()
    parent = {}
    point_gcost = {}
    point_hcost = {}
    point_fcost = {}
    
    # Initialise current
    current = start
    frontier.add(current)
    point_gcost[current] = 0
    point_fcost[current] = 2  # initialize based on initial neighbor fcost
    parent[current] = None
 
    #while there is possible path in frontier
    while frontier:

        current = min(frontier, key=lambda x:point_fcost[x])
        
        # reach goal, trace path
        if current == goal:
            path = []
            while parent[current]:
                path.append(current)
                current = parent[current]
            path.append(current)
            # invert path and return
            return path[::-1]
        
        # reached and tested
        frontier.remove(current)
        explored.add(current)    
        
        # neighbour checks
        for node in M.roads[current]:
            if node in explored:
                continue
            if node in frontier:
                new_gcost = point_gcost[current] + gcost(M, node, current)
                # compare and update gcost 
                if point_gcost[node] > new_gcost:
                    point_gcost[node] = new_gcost
                    point_fcost[node] = point_gcost[node] + point_hcost[node]
                    parent[node] = current
            else:
                # calculate fcost/gcost/hcost and parent
                point_gcost[node] = point_gcost[current] + gcost(M, node, current)
                point_hcost[node] = hcost(M, node, goal)
                point_fcost[node] = point_gcost[node] + point_hcost[node]
                parent[node] = current
                frontier.add(node)
        
def gcost(M, node1, node2):
    nodeone = M.intersections[node1]
    nodetwo = M.intersections[node2]
    a = abs(nodeone[0] - nodetwo[0]) 
    b = abs(nodeone[1] - nodetwo[1]) 
    g_cost = math.sqrt((a ** 2) + (b ** 2))
    return g_cost
                    
def hcost(M, node, goal):
    nodetwo = M.intersections[goal]
    nodeone = M.intersections[node]
    x = abs(nodeone[0] - nodetwo[0])
    y = abs(nodeone[1] - nodetwo[1])
    h_cost = math.sqrt((x ** 2) + (y ** 2))
    return h_cost
