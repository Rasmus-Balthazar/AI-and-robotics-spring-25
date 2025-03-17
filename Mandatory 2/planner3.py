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


def bfs(player, goals, walls, boxes):
    visited = set()
    queue = Kueue()
    moves = []
    queue.enqueue((player, moves))
    visited.add(player)
    directions = [(0,1), (0,-1), (1,0), (-1,0)] #right, left, down, up
    while not queue.is_empty():
        current, moves = queue.dequeue()
        #where can the player move
        for direction in directions:
            new_position = (current[0] + direction[0], current[1] + direction[1])
            #if the new position is a wall, or it has already been visited
            if new_position in walls or new_position in visited:
                continue #we can't move here, don't add it to the queue
            #if the new position is a goal
            if new_position in goals:
                return moves #we have reached the goal
            #if the new position is a box
            if new_position in boxes:
                #where can the box move
                box_position = (new_position[0] + direction[0], new_position[1] + direction[1])
                #if the box can move
                if box_position not in walls and box_position not in boxes:
                    #update the position of the box
                    boxes.remove(new_position)
                    boxes.add(box_position)
                    #update the position of the player
                    player = new_position
                    #add the move to the list of moves
                    moves.append(direction)
                    #add the new position to the queue
                    queue.enqueue((player, moves))
                    visited.add(player)
            else:
                #if the new position is empty
                player = new_position
                moves.append(direction)
                queue.enqueue((player, moves))
            visited.add(new_position)
    return moves
            


# Claire
input = """#######
#.@ # #
#$* $ #
#   $ #
# ..  #
#  *  #
#######"""
input_simple = """#######
#.@   #
#$    #
#     #
#     #
#     #
#######"""
p, g, w, b = read_input(input_simple)
print(p)
print(g)
print(w)
print(b)
print("Solution: ------------------")
print(bfs(p, g, w, b))