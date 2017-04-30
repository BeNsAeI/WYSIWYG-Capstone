# Module detail:
# This file describes the Block GUI class
# Objects of such class have the following attributes:
# - Name
# - Type
# - Caption
# - ID
# This file also contains the tests for the Block module

class Block:
	def __init__(self,name,type,caption,id,value):
		self.Name=name
		self.Type=type
		self.Caption=caption
		self.ID=id
		self.Value=value

	def changeName(self,name):
		self.Name=name
	def changeType(self,type):
		self.Type=type
	def changeCaption(self,caption):
		self.Caption=caption
	def changeID(self,id):
		self.ID=id
	def changeAddress(self,addr):
		self.Address=addr
def testCase():
	import random
	print("Test case:")
	name="Test"
	type="Func"
	caption="Test function"
	id=0
	des="New descriptio"
	addr="New address"
	print("Make an object atrebutes: \""+name+"\", \""+type+"\", \""+caption+"\", "+str(id)+".")
	a=Block(name,type,caption,id,0)
	print("checking attrebutes: ")
	if (a.Name == name):
		print("self.Name: "+"\t"+'\033[1;32m'+"Pass"+'\033[1;m')
	else:
		print("self.Name: "+"\t"+'\033[1;31m'+"Fail"+'\033[1;m')
	if (a.Type == type):
		print("self.Type: "+"\t"+'\033[1;32m'+"Pass"+'\033[1;m')
	else:
		print("self.Type: "+"\t"+'\033[1;31m'+"Fail"+'\033[1;m')
	if (a.Caption == caption):
		print("self.Caption: "+"\t"+'\033[1;32m'+"Pass"+'\033[1;m')
	else:
		print("self.Caption: "+"\t"+'\033[1;31m'+"Fail"+'\033[1;m')
	if (a.ID == id):
		print("self.ID: "+"\t"+'\033[1;32m'+"Pass"+'\033[1;m')
	else:
		print("self.ID: "+"\t"+'\033[1;31m'+"Fail"+'\033[1;m')

	print("___")
	print("Changing name:")
	name="new_"+name
	a.changeName(name)
	if (a.Name == name):
		print("self.Name: "+"\t"+'\033[1;32m'+"Pass"+'\033[1;m')
	else:
		print("self.Name: "+"\t"+'\033[1;31m'+"Fail"+'\033[1;m')
	a.changeType(type)
	if (a.Type == type):
		print("self.Type: "+"\t"+'\033[1;32m'+"Pass"+'\033[1;m')
	else:
		print("self.Type: "+"\t"+'\033[1;31m'+"Fail"+'\033[1;m')
	a.changeCaption(caption);

	a.changeAddress(addr);
	if(a.Address == addr):
		print("self.Address: "+"\t"+'\033[1;32m'+"Pass"+'\033[1;m')
	else:
		print("self.Address: "+"\t"+'\033[1;31m'+"Fail"+'\033[1;m')

testCase()
