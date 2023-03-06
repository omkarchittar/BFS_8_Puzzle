
# Test case 1:
nodeInitial = [1,6,7], [2,0,5], [4,3,8]
nodeGoal = [1,4,7], [2,5,8], [3,0,6]

#Test case 2:
# nodeInitial = [4,7,8], [2,1,5], [3,6,0]
# nodeGoal = [1,4,7], [2,5,8], [3,6,0]

def column2row(nodeInitial, nodeGoal):
    state1 = []
    state2 = []

    for i in range(3):
        for j in range(3):
            state1.append(nodeInitial[j][i])

    for i in range(3):
        for j in range(3):
            state2.append(nodeGoal[j][i])

    return state1, state2

# function for printing the path taken to reach the nodeGoal in nodePath.txt 
def print_nodes(path, nodeState, NodesInfo):
    f =  open("nodePath.txt", "w+")  #opens the file in writing mode
    for i in range(len(path)):
        for j in [0,3,6,1,4,7,2,5,8]:
            f.write(str(path[i][j]))
            f.write(" ")
        f.write("\n")
    f.close()

# printing all the nodes visited in Nodes.txt
    f = open("Nodes.txt", "w+")
    for i in range(len(nodeState)):
        for j in range(len(nodeState[0])):
            f.write(str(nodeState[i][j]))
            f.write(" ")
        f.write("\n")
    f.close()

# printing all the nodes visited along with their nodeNumber and parentIndex
    f = open("NodesInfo.txt", "w+")
    for i in range(len(NodesInfo)):
        f.write(str(NodesInfo[i]))
        f.write("\n")
    f.close()

    print("Printing Successful!\nCheck 'Nodes.txt' and 'NodesInfo.txt'")

# function for swapping tiles while moving the blank tile 
def swap_tiles(node, index, next_index):
    node[index], node[next_index] = node[next_index], node[index]
    return node

# function for getting the current position of the blank tile
def state(node):
    blank_col = int(node.index(0)%3) + 1
    blank_row = int(node.index(0)/3) + 1
    pos = (blank_row, blank_col)
    return pos

# function to move the tile to the left
def shiftLeft(node):
    position = state(node)
    index = node.index(0)
    if(position[1]==1):
        status = False
        newNode = node
    else:
        status = True
        newNode = swap_tiles(node.copy(), index, index-1)

    return status, newNode

# function to move the tile upwards
def shiftRight(node):
    position = state(node)
    index = node.index(0)
    if(position[1]==3):
        status = False
        newNode = node
    else:
        status = True
        newNode = swap_tiles(node.copy(), index, index+1)
    return status, newNode

# function to move the tile to the right
def shiftUp(node):
    position = state(node)
    index = node.index(0)
    if(position[0]==1):
        status = False
        newNode = node
    else:
        status = True
        newNode = swap_tiles(node.copy(), index, index-3)
    return status, newNode

# function to move the tile downwards
def shiftDown(node):
    position = state(node)
    index = node.index(0)
    if(position[0]==3):
        status = False
        newNode = node
    else:
        status = True
        newNode = swap_tiles(node.copy(), index, index+3)
    return status, newNode

# function for generating the path taken from nodeInitial to nodeGoal
def generate_path(nodeState, visited_nodes):
    path = []
    path.append(nodeState[-1])

    parent_index = len(nodeState)

    while(path[-1]!=nodeState[0]):
        parent_index = visited_nodes[parent_index-1][1]
        val = visited_nodes[parent_index-1][2]
        path.append(val)

    path.reverse()
    return path

# algorithm to perform the search operation
# movement priorities are : Left -> Up -> Right -> Down
def BFS_algo(nodeInitial, nodeGoal):
    nodeState = []
    visited_nodes = []

    nodeState.append(nodeInitial)
    visited_nodes.append([1, 0, nodeInitial])

    nodeIndex = 2
    parentIndex = 0

    currentNode = nodeInitial.copy()

    # repeat till nodeGoal is reached
    # check if a given shift is possible
    while(1):
        status, newNode = shiftLeft(currentNode.copy())
        if(status==True and newNode not in nodeState):
            nodeState.append(newNode)
            visited_nodes.append([nodeIndex, parentIndex+1, newNode])
            nodeIndex = nodeIndex + 1
            if(newNode == nodeGoal):
                break

        status, newNode = shiftUp(currentNode.copy())
        if(status==True and newNode not in nodeState):
            nodeState.append(newNode)
            visited_nodes.append([nodeIndex, parentIndex+1, newNode])
            nodeIndex = nodeIndex + 1
            if(newNode == nodeGoal):
                break

        status, newNode = shiftRight(currentNode.copy())
        if(status==True and newNode not in nodeState):
            nodeState.append(newNode)
            visited_nodes.append([nodeIndex, parentIndex+1, newNode])
            nodeIndex = nodeIndex + 1
            if(newNode == nodeGoal):
                break

        status, newNode = shiftDown(currentNode.copy())
        if(status==True and newNode not in nodeState):
            nodeState.append(newNode)
            visited_nodes.append([nodeIndex, parentIndex+1, newNode])
            nodeIndex = nodeIndex + 1
            if(newNode == nodeGoal):
                break

        parentIndex = parentIndex + 1
        currentNode = nodeState[parentIndex]

    return nodeState, visited_nodes

state1, state2 = column2row(nodeInitial, nodeGoal)
nodeState, visited_nodes = BFS_algo(state1, state2)

# generating the path
path = generate_path(nodeState, visited_nodes)

# printing the values in 'Nodes.txt' and 'NodesInfo.txt'
print_nodes(path, nodeState, visited_nodes)
