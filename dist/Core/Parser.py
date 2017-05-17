# This core file has the purpose of Parsing the computer readable data into appropriate data structure
# The input is the tokens and it generates the tree

class Tree:
	def __init__(self,curr):
		self.Curr = curr
		self.Next = None
		self.Prev = None
	def N(self,tmp):
		self.Next = tmp
	def P(self,tmp):
		self.Prev = tmp

class Parser:
	def __init__(self):
		self.hasMembers = False
		self.StartNode = None;
		self.current = self.StartNode;
		self.numNodes = 0;
	def __Start():
		self.StartNode = Tree();
		return self.StartNode
	def __addNode(address,argsList):
		self.numNodes += 1;
		self.hasMembers = True;
		Node = Tree();
		return Node;
	def __Term():
		return None;
	def getTree():
		return self.StatNode;

def testCase():
	print("Testing: ");
testCase()
