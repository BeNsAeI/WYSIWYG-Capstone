#setting up the path:
class projectPath:
	def __init__(self):
		self.path = ""
		self.outputPath = self.path+"Output.py"
	def updatePath(self, textinput):
		self.path = textinput
		self.outputPath = self.path+"Output.py"
	def getPath(self):
		return self.outputPath