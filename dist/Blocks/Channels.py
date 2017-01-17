# Module detail:
# This file describes the Channel GUI class
# Objects of such class have the following attributes:
# This file also contains the tests for the Block module
class Channel:
	def __init__(self,source,destination,data):
		self.SourceID=source
		self.DestinationID=destination
		self.Data=data;
	def changeSource(self,source):
		self.SourceID=source
	def changeDestination(self,destination):
		self.DestinationID=destination
	def In(data):
		seld.Data=data
	def Out():
		return self.Data
def testCase():
	import random
	print("Test case:")
	source=random.randint(1, 10)
	destination=random.randint(1, 10)
	data=random.randint(1,10)
	print("Source ID is: "+str(source)+".")
	print("Destination ID is: "+str(destination)+".")
	print("Data is: "+str(data)+".")
	C_ab=Channel(source,destination,data)
	if (C_ab.SourceID == source):
		print("initial self.SourceID: "+"\t"+'\033[1;32m'+"Pass"+'\033[1;m')
	else:
		print("initial self.SourceID: "+"\t"+'\033[1;31m'+"Fail"+'\033[1;m')
	if (C_ab.DestinationID == destination):
		print("initial self.DestinationID: "+"\t"+'\033[1;32m'+"Pass"+'\033[1;m')
	else:
		print("initial self.DestinationID: "+"\t"+'\033[1;31m'+"Fail"+'\033[1;m')
	if (C_ab.Data == data):
		print("initial self.Data: "+"\t"+'\033[1;32m'+"Pass"+'\033[1;m')
	else:
		print("initial self.Data: "+"\t"+'\033[1;31m'+"Fail"+'\033[1;m')
testCase()
