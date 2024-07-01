f = open("./inputs/day-12-input.txt")
input = f.read().splitlines()

class Heightmap:
    def __init__(self, input: list[str]) -> None:
        self.content = input
        self.width = len(self.content[0])
        self.height = len(self.content)
        self.visited = set()
        self.start, self.end = self.find_start_and_end()
    
    def __str__(self) -> str:
        res = ""
        for  i in self.content:
            for j in i:
                res += j
            res += "\n"
        return res
    
    # TODO this should probably return a dict
    def find_start_and_end(self) -> list[tuple[int, int]]:
        '''Returns the coordinates of the start and end position as two (x,y) tuples inside of a list.'''
        start_end = [None, None]
        y = 0
        while y < self.height and None in start_end:
            x = 0
            while x < self.width and None in start_end:
                val = self.content[y][x]
                if val == "S":
                    start_end[0] = (x, y)
                elif val == "E":
                    start_end[1] = (x, y)
                x += 1
            y += 1
        return start_end
    
    def elevation_at(self, position: tuple[int, int]) -> str:
        '''Return the elevation of a position as an integer.'''
        x = position[0]
        y = position[1]
        elev = self.content[y][x]
        if elev == "S":
            return ord("a")
        elif elev == "E":
            return ord("z")
        else:
            return ord(elev)
        
    def true_value_at(self, pos: tuple[int, int]) -> str:
        x, y = pos
        return self.content[y][x]
        
    def pos_in_bounds(self, pos: tuple[int, int]) -> bool:
        return pos[0] >= 0 and pos[1] >= 0 and pos[0] < self.width and pos[1] < self.height
    
    def elevation_dif(self, pos_A: tuple[int, int], pos_B: tuple[int, int]) -> bool:
        elevation_A = self.elevation_at(pos_A)
        elevation_B = self.elevation_at(pos_B)
        return elevation_B - elevation_A

    def find_candidates(self, pos: tuple[int, int], reverse_dir: bool = False) -> list[tuple[int, int]]:
        '''Returns a list of unvisited positions that are adjacent and reachable from a given position. Optionally reverse the elevation rules.'''
        candidates = []
        delta_x = [0,  0,  1, -1]
        delta_y = [1, -1,  0,  0]
        for dir in range(4):
            new_pos = (pos[0] + delta_x[dir], pos[1] + delta_y[dir])
            if self.pos_in_bounds(new_pos) and new_pos not in self.visited:
                if (not reverse_dir and self.elevation_dif(pos, new_pos) <= 1
                    or reverse_dir and self.elevation_dif(pos, new_pos) >= -1):
                    candidates.append(new_pos)
                    self.visited.add(new_pos)
        return candidates

    def bfs(self, start_pos: tuple[int, int], search_val: str, reverse_dir: bool = False) -> int:
        '''A breadth-first search algorithm returning the length of the shortest path between a start point and the closest occurence of a search value. Optionally reverse elevation traversal rules.'''
        self.visited = set() # reset visited set
        queue = [(start_pos, 0)]
        self.visited.add(start_pos)
        while queue:
            current_pos = queue[0][0]
            current_depth = queue[0][1]
            if self.true_value_at(current_pos) == search_val:
                return current_depth
            else:
                removed = queue.pop(0)[0]
                new_candidates = self.find_candidates(removed, reverse_dir)
                queue.extend([(c, current_depth + 1) for c in new_candidates])

    def shortest_path_length_S_to_E(self) -> int:
        return self.bfs(self.start, "E")
    
    def shortest_path_length_E_to_any_a(self) -> int:
        return self.bfs(self.end, "a", True)
        

hm = Heightmap(input)
print(f"Shortest path from start S to end E: {hm.shortest_path_length_S_to_E()}")
print(f"Shortest path from any elevation a to E: {hm.shortest_path_length_E_to_any_a()}")