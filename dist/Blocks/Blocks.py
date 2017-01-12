# Module detail:
# This file describes the Block GUI class
# Objects of such class have the following attributes:
# - Name
# - Type
# - Caption
# - ID
# - Size
# - Position
# This file also contains the tests for the Block module

class Block:
	def __init__(self,name,type,caption,id,w,h,x=0,y=0):
		self.Name=name
		self.Type=type
		self.Caption=caption
		self.ID=id
		self.Size=[w,h]
		self.Position=[x,y]
	def changeName(self,name):
		self.Name=name
	def changeType(self,type):
		self.Type=type
	def changeCaption(self,caption):
		self.Caption=caption
	def changeID(self,id):
		self.ID=id
	def changeSize(self,w,h):
		self.Size=[w,h]
	def changePosition(self,x,y):
		self.Position=[x,y]
	def changeDescription(self,des):
		self.Description=des
	def changeAddress(self,addr):
		self.Address=addr
def testCase():
	import random
	print("Test case:")
	name="Test"
	type="Func"
	caption="Test function"
	id=0
	w=random.randint(1, 10)
	h=random.randint(1, 10)
	x=random.randint(1, 10)
	y=random.randint(1, 10)
	print("Make an object atrebutes: \""+name+"\", \""+type+"\", \""+caption+"\", "+str(id)+", "+str(w)+", "+str(h)+", "+str(x)+", "+str(y)+".")
	a=Block(name,type,caption,id,w,h,x,y)
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
	if (a.Size[0] == w):
		print("self.Size[0]: "+"\t"+'\033[1;32m'+"Pass"+'\033[1;m')
	else:
		print("self.Size[0]: "+"\t"+'\033[1;31m'+"Fail"+'\033[1;m')
	if (a.Size[1] == h):
		print("self.Size[1]: "+"\t"+'\033[1;32m'+"Pass"+'\033[1;m')
	else:
		print("self.Size[1]: "+"\t"+'\033[1;31m'+"Fail"+'\033[1;m')
	if (a.Position[0] == x):
		print("self.Position[0]: "+"\t"+'\033[1;32m'+"Pass"+'\033[1;m')
	else:
		print("self.Position[0]: "+"\t"+'\033[1;31m'+"Fail"+'\033[1;m')
	if (a.Position[1] == y):
		print("self.Position[1]: "+"\t"+'\033[1;32m'+"Pass"+'\033[1;m')
	else:
		print("self.Position[1]: "+"\t"+'\033[1;31m'+"Fail"+'\033[1;m')
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
	a.changeCaption(caption)
	if (a.Caption == caption):
		print("self.Caption: "+"\t"+'\033[1;32m'+"Pass"+'\033[1;m')
	else:
		print("self.Caption: "+"\t"+'\033[1;31m'+"Fail"+'\033[1;m')
	a.changeID(id)
	if (a.ID == id):
		print("self.ID: "+"\t"+'\033[1;32m'+"Pass"+'\033[1;m')
	else:
		print("self.ID: "+"\t"+'\033[1;31m'+"Fail"+'\033[1;m')
	a.changeSize(w,h)
	if (a.Size[0] == w):
		print("self.Size[w]: "+"\t"+'\033[1;32m'+"Pass"+'\033[1;m')
	else:
		print("self.Size[w]: "+"\t"+'\033[1;31m'+"Fail"+'\033[1;m')
	if (a.Size[1] == h):
		print("self.Size[h]: "+"\t"+'\033[1;32m'+"Pass"+'\033[1;m')
	else:
		print("self.Size[h]: "+"\t"+'\033[1;31m'+"Fail"+'\033[1;m')

testCase()
