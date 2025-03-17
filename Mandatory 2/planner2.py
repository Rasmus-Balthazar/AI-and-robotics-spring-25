def sokoban_bfs(grid, start):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    visited = set()
    queue = [start]  # Using a list instead of deque
    visited.add(start)
    
    while queue:
        r, c = queue.pop(0)  # Using list pop(0) instead of deque.popleft()
        print(f"Player at: ({r}, {c})")
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                if grid[nr][nc] in {' ', '.'}:  # Walkable spaces
                    queue.append((nr, nc))
                    visited.add((nr, nc))
                elif grid[nr][nc] == '$':  # Box detected
                    box_nr, box_nc = nr + dr, nc + dc  # Next box position
                    if 0 <= box_nr < rows and 0 <= box_nc < cols and grid[box_nr][box_nc] in {' ', '.'}:
                        queue.append((nr, nc))  # Player can move here
                        visited.add((nr, nc))

# Example Sokoban grid
sokoban_grid = [
    ['#', '#', '#', '#', '#'],
    ['#', ' ', '@', '$', '#'],
    ['#', ' ', ' ', '.', '#'],
    ['#', '#', '#', '#', '#']
]

# Find player's starting position
player_start = None
for i in range(len(sokoban_grid)):
    for j in range(len(sokoban_grid[0])):
        if sokoban_grid[i][j] == '@':
            player_start = (i, j)
            break
    if player_start:
        break

# Run BFS
if player_start:
    sokoban_bfs(sokoban_grid, player_start)
