from __future__ import annotations
# (necessary for Position.touches() to take object of own class as argument)

f = open("./day-09-input.txt")
input = f.read().splitlines()
motions = [motion.split() for motion in input]

for ix, i in enumerate(motions):
    for jx, j in enumerate(i):
        if j.isdigit(): motions[ix][jx] = int(j)
    motions[ix] = tuple(motions[ix])

class Position:
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]
    def touches(self, other: Position) -> bool:
        return self.has_x_adjacent_or_same_to(other) and self.has_y_adjacent_or_same_to(other)
    def has_x_adjacent_or_same_to(self, other):
        return self.x in [other.x - 1, other.x, other.x + 1]
    def has_y_adjacent_or_same_to(self, other):
        return self.y in [other.y - 1, other.y, other.y + 1]

class Head(Position):
    def __init__(self, pos, tail_count):
        super().__init__(pos)
        self.tail = Tail(pos, tail_count, self)
        self.visited_by_last_tail = {(self.x, self.y)}
    def total_visited_by_last_tail(self):
        return len(self.visited_by_last_tail)
    def move(self, direction):
        match direction:
            case "R": self.x += 1
            case "L": self.x += -1
            case "U": self.y += 1
            case "D": self.y += -1
        if not self.touches(self.tail):
            self.tail.drag(self)

class Tail(Position):
    def __init__(self, pos, tail_count, head:Head):
        super().__init__(pos)
        self.head = head
        self.tail = None
        if tail_count > 1:
            self.tail = Tail(pos, tail_count - 1, head)
    def drag(self, parent:Position):
        if parent.has_x_adjacent_or_same_to(self):
            self.x = parent.x
            if parent.y < self.y: self.y = parent.y + 1
            else: self.y = parent.y - 1
        elif parent.has_y_adjacent_or_same_to(self):
            self.y = parent.y
            if parent.x < self.x: self.x = parent.x + 1
            else: self.x = parent.x - 1
        else:
            self.drag_diagonally_to(parent)
        if self.tail is not None and not self.touches(self.tail):
            self.tail.drag(self)
        elif self.tail is None:
            self.head.visited_by_last_tail.add((self.x, self.y))
    def drag_diagonally_to(self, parent:Position):
        if parent.x < self.x: self.x += -1
        else: self.x += 1
        if parent.y < self.y: self.y += -1
        else: self.y += 1


starting_pos = (0, 0)
head = Head(starting_pos, 1)
head2 = Head(starting_pos, 9)

for motion in motions:
    direction = motion[0]
    steps = range(motion[1])
    for step in steps:
        head.move(direction)
        head2.move(direction)

print(head.total_visited_by_last_tail())
print(head2.total_visited_by_last_tail())