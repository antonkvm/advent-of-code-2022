from functools import reduce


with open("./inputs/day-07-input.txt") as f:
	input = f.read().splitlines()

	class Node:
		def __init__(self, name:str, isDir:bool, size=0, parent:object=None):
			self.name = name
			self.isDir = isDir
			self.size = size
			self.parent = parent
			self.children = []

		def addChild(self, child_node):
			self.children.append(child_node)
			self.update_ancestor_sizes(child_node.size)

		# increase the sizes of self and all ancestors with a given value:
		def update_ancestor_sizes(self, value):
			self.size += value
			if self.parent: self.parent.update_ancestor_sizes(value)

		# traverse tree and sum up all directory sizes that are below or equal to a given max value:
		# (Postorder Depth-First Search)
		def traverse_and_sum_sizes(self, max):
			res = sum([child.traverse_and_sum_sizes(max) for child in self.children if child.isDir])
			return res + self.size if self.size <= max else res
		
		# recursively traverse the tree, finding the smallest directory size above a given treshhold:
		# (Preorder Depth-First Search)
		def find_min_above_threshhold(self, threshhold, current_min=None):
			if self.isDir and self.size >= threshhold:
				if current_min == None or self.size < current_min:
					current_min = self.size
			for child in self.children:
				current_min = child.find_min_above_threshhold(threshhold, current_min)
			return current_min 
		

	# build the file system tree:

	root = Node(isDir=True, name="/")
	currentNode = root

	for l in input[1:]:
		if l[0:4] == "$ ls":
			continue
		elif l[0:4] == "$ cd":
			targetDir = l[5:]
			if targetDir != "..":
				for child in currentNode.children:
					if child.name == targetDir and child.isDir == True:
						currentNode = child
						break
			else: currentNode = currentNode.parent
		else:
			if l[0:3] == "dir":
				currentNode.addChild(Node(isDir=True, name=l[4:], parent=currentNode))
			else:
				name = l.split()[1]
				size = int(l.split()[0])
				currentNode.addChild(Node(isDir=False, name=name, size=size, parent=currentNode))


	# output results:

	print(root.traverse_and_sum_sizes(max=100000))

	total_space = 70000000
	free_space = total_space - root.size
	needed_space = 30000000
	# find the smallest directory still large enough to free up enough space when deleted:
	print(root.find_min_above_threshhold(needed_space - free_space))