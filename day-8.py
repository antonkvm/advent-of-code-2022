f = open("./day-8-input.txt")
forest = f.read().splitlines()
forest = [[int(tree) for tree in row] for row in forest]

# Part 1:

rows = len(forest)
cols = len(forest[0])
edge_trees = rows * 2 + cols * 2 - 4
visible_trees = edge_trees

def check_direction(row, col, direction) -> bool:
    current_tree = forest[row][col]
    only_shorter_trees = False
    match direction:
        case "left": search_range = range(col - 1, -1, -1)
        case "right": search_range = range(col + 1, cols, 1)
        case "up":  search_range = range(row - 1, -1, -1)
        case "down": search_range = range(row + 1, rows, 1)
        case _: raise Exception("Invalid input: Direction must be left, right, up, or down.")
    if direction in ["left", "right"]:
         for i in search_range:
            if forest[row][i] >= current_tree: return False
            else: only_shorter_trees = True
    elif direction in ["up", "down"]:
        for i in search_range:
            if forest[i][col] >= current_tree: return False
            else: only_shorter_trees = True
    return only_shorter_trees

def check_tree_visibility(row, col) -> bool:
    for direction in ["left", "right", "up", "down"]:
        if check_direction(row, col, direction): return True

for row in range(1, rows - 1):
    for col in range(1, cols - 1):
        if check_tree_visibility(row, col) == True:
            visible_trees += 1
            
print(f"Visible trees = {visible_trees}")

# Part 2:

def get_scenic_score(row, col) -> int:
    result = 1
    for direction in ["left", "right", "up", "down"]:
        result *= get_view_distance(row, col, direction)
    return result

def get_view_distance(row, col, direction) -> int:
    current_tree_height = forest[row][col]
    viewing_distance = 0
    match direction:
        case "left": search_range = range(col - 1, - 1, -1)
        case "right": search_range = range(col + 1, cols, 1)
        case "up":  search_range = range(row -1, -1, -1)
        case "down": search_range = range(row + 1, rows, 1)
        case _: raise Exception("Invalid input: Direction must be left, right, up, or down.")
    if direction in ["left", "right"]:
        for i in search_range:
            if forest[row][i] >= current_tree_height:
                viewing_distance += 1
                return viewing_distance
            else:
                viewing_distance += 1
    elif direction in ["up", "down"]:
        for i in search_range:
            if forest[i][col] >= current_tree_height:
                viewing_distance += 1
                return viewing_distance
            else:
                viewing_distance += 1
    return viewing_distance

scenic_highscore = 0
for row in range(rows):
    for col in range(cols):
        current_tree_scenic_score = get_scenic_score(row, col)
        if current_tree_scenic_score > scenic_highscore:
            scenic_highscore = current_tree_scenic_score

print(f"Highest scenic score: {scenic_highscore}")