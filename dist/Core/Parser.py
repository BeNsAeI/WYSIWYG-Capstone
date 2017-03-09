# This core file has the purpose of Parsing the computer readable data into appropriate data structure
# The input is the tokens and it generates the tree
# Grammar:
#	Start -> succ
#	succ -> block succ | terminate | empty
#	block -> <INSERT LIST OF RECOGNIZED BLOCKS>
#	terminate -> empty

from . import Token

class Start:
	def __init__(self):
		self.sent = None

class End:
	def __init__(self):
		self.sent = 0

class Tree:
	def __init__(self):
		self.Right = None
		self.Left = None
		self.Center = None
		self.Sibiling = None
		self.Data = None

class Parser:
	def __init__(self):
		self.hasMembers = False
	def __BuidTree():
		
	def __Start():
		return (Start node)
	def __Succ():
		
	def __Block():
		
	def __Terminate();
		
	def getTree():
		
def testCase():
	print("Testing: ");
testCase()
