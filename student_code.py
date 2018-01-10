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
    point_hcost[current] = cost(M, start, goal)
    point_fcost[current] = point_gcost[current] + point_hcost[current]
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
                continue
            if node in frontier:
                new_gcost = point_gcost[current] + cost(M, node, current)
                # compare and update gcost 
                if point_gcost[node] > new_gcost:
                    point_gcost[node] = new_gcost
                    point_fcost[node] = point_gcost[node] + point_hcost[node]
                    parent[node] = current
            else:
                # calculate fcost/gcost/hcost and parent
                point_gcost[node] = point_gcost[current] + cost(M, node, current)
                point_hcost[node] = cost(M, node, goal)
                point_fcost[node] = point_gcost[node] + point_hcost[node]
                parent[node] = current
                frontier.add(node)

                        
def cost(M, node1, node2):
    nodeone = M.intersections[node1]
    nodetwo = M.intersections[node2]
    a = nodeone[0] - nodetwo[0] 
    b = nodeone[1] - nodetwo[1] 
    cost = math.sqrt((a ** 2) + (b ** 2))
    return cost
                    
