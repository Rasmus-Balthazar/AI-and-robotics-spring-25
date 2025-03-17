from kueue import Kueue

#reader
def read_input(input):
    tasks = []
    player_index = (0,0)
    #boxes can be updated whereas the rest cannot
    goals = set()
    walls = set()
    boxes = set()
    input_split = input.split("\n")
    for(i, line) in enumerate(input_split):
        for(j, char) in enumerate(line):
            if(char == "@"):
                player_index = (i,j)
            if(char == "$"):
                boxes.add((i,j))
            if(char == "." or char == "*"):
                goals.add((i,j))
            if(char == "#"):
                walls.add((i,j))
    return player_index, goals, walls, boxes

class Node:
    def __init__(self, s, c, p):
        state = s # state, what is our current index + move for how we got here. tuple 
        children = c
        parent = p 
class Tree:
    def __init__(self, start_state):
        root = start_state 
def bfs(player, goals, walls, boxes):
    visited = set()
    queue = Kueue()
    moves = []
    queue.enqueue((player, moves))
    visited.add(player)
    root = Node(player, [], [])
    tree = tree(root)
    path = []
    directions = [(0,1), (0,-1), (1,0), (-1,0)] #right, left, down, up
    
    #FIXME: add the path to the queue
    #FIXME: add the path to the visited set
    #FIXME: push boxes
    #FIXME: Change goal to be pushing boxes into the goal
    while not queue.is_empty():
        current, moves = queue.dequeue()
        #where can the player move
        tmp = Node((current, moves),[],[])
        for direction in directions:
            new_position = (current[0] + direction[0], current[1] + direction[1])
            #if the new position is a wall, or it has already been visited
            n = Node((new_position, direction), [], tmp)
            if new_position in walls or new_position in visited:
                continue #we can't move here, don't add it to the queue
            #if the new position is a goal
            if new_position in goals:
                return moves, path #we have reached the goal
                #alternatively check if there are no boxes left = win!
            #if the new position is a box
            if new_position in boxes:
                #where can the box move
                box_position = (new_position[0] + direction[0], new_position[1] + direction[1])
                #if the box can move
                if box_position not in walls and box_position not in boxes:
                    # a box must never be pushed into a corner, check if box is in a corner now
                    #update the position of the box
                    boxes.remove(new_position)
                    boxes.add(box_position)
                    #update the position of the player
                    player = new_position
                    
                    
                    #add the move to the list of moves
                    moves.append(direction)
                    #add the new position to the queue
                    new_pos_node = Node((player, moves), [], tmp)
                    queue.enqueue((player, moves))
                    path.append((new_position, direction))
                    visited.add(player)
            else:
                #if the new position is empty
                player = new_position
                moves.append(direction)
                queue.enqueue((player, moves))
                path.append(new_position)
            visited.add(new_position)
    return moves, path
            


# Claire
input = """#######
#.@ # #
#$* $ #
#   $ #
# ..  #
#  *  #
#######"""
input_simple = """#######
#.    #
#$    #
#     #
#     #
#  @  #
#######"""
p, g, w, b = read_input(input_simple)
print(p)
print(g)
print(w)
print(b)
print("Solution: ------------------")
moves, path = bfs(p, g, w, b)

print(path)
print(moves)