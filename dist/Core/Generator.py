# This Core file generates and outputs the python file based on the data structure
# Initiate generator using constructor (it starts the EXECUTION())
# For each element in table of execution:
# 1: Get the function from list
# 2: Get the parametters from execution tree using the channel ID
# 3: generate and format the line
# 4: Open the output file
# 5: Add the string to the file
# 6: close the file
# de struct the program which Calls the EXECUTION()
from TemplateHandler import fileIO
class Generator:
	def __init__(self,first=False):
		self.spaghetti = ''
		if first:
			self.spaghetti = '# Generate with Tensorflow WYSIWYG GUI\nimport tensorflow as tf\nimport numpy as np\nimport matplotlib.pyplot as plt\n'
		pass
		#add import * from *
		#add import HO from Source.py
		#add def EXECUTION(argc,argv):
	def generate():
		pass
		#Generating the code for the tool
	def __del__(self):
		pass
		#add EXECUTION(len(sys.argv),sys.argv)
	def addBlock(self,name,II,args,comment):
		input = fileIO("python")
		newBlock = input.read_fil(name)
		for i in range (0,100):
			indent = ''
			for j in range(0,i+II):
				indent += '\t'
			newBlock = newBlock.replace('#'+str(i)+'#',indent)
		for i in range(0, len(args)):
			word = args[i]
			word = word.replace('.','_')
			newBlock = newBlock.replace('<<ARG'+str(i)+'>>',word)
		newBlock = newBlock.replace('<<COM>>',comment)
		self.spaghetti += newBlock
	def release(self,path="Output.py"):
		self.spaghetti += '\n'
		output = fileIO("python")
		output.writefil(self.spaghetti,path)

def testCase():
	II = 0;
	temp = Generator()

	comment = "This is a variable declearation"
	varName = "string"
	varValue='"Hello world!"'
	args=[varName,varValue]
	temp.addBlock("var",II,args,comment)

	comment = "This is a variable declearation"
	varName = "x"
	varValue="10"
	args=[varName,varValue]
	temp.addBlock("var",II,args,comment)

	comment = "This is a comment made by Ben"
	tempLoop = "i"
	arrayName = "range(0,x)"
	todoThing = ""
	args=[tempLoop,arrayName,todoThing]
	temp.addBlock("for",II,args,comment)

	II+=1
	comment = 'testing print'
	varName = 'i'
	args=[varName]
	temp.addBlock("print",II,args,comment)

	print(temp.spaghetti)
	temp.release()
	pass
testCase()
