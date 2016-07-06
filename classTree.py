class Tree():
	def __init__(self, species, size):
		self.species = species
		#size is an integer in feet
		self.size = size
'''	def grow(self, size):
		#grow certain amount in inches every year
		if treeNum1:
			self.height += 5
		elif treeNum2:
			self.height += 2
		elif treeNum3:
			size += 0
		elif treeNum4:
			size += 500
	'''
	def water(self):
		#each tree given same amount of water, but each reacts differently
		treeNum1 = print("Yay! Wata wata wata!!!")
		treeNum2 = print("luv the H20")
		treeNum3 = print("Do you really think water is going to make me grow?")
		treeNum4 = print("I don't need no aqua")

		

#______________________________________________________________

class ChristmasTree(Tree):
	def __init__(self, species, size, ornaments, tinsel, star):
		self.ornaments = ornaments
		self.tinsel = tinsel
		self.star = star
		Tree.__init__(self, species, size)
	
	def presents(self):
		print("Merry christmas, here are your presents!")
		
	def rudolph(self):
		print("Rudolph then red-nosed reindeer is gonna save the day! whoo")





treeNum1 = Tree("This tree is an Apple Tree", 50)
treeNum2 = Tree("This tree is an Orange Tree", 27)
treeNum3 = Tree("This tree is the tree from Charlie Brown", 2)
treeNum4 = Tree("This tree is the Giant's Tree from Jack & The Beankstalk", 700)
myChristmasTree = ChristmasTree("Christmas Tree", "Big", "Red and Blue Ornaments", "Gold Tinsel", "Glowing Star")

print(treeNum2.type)
print(myChristmasTree.ornaments)
