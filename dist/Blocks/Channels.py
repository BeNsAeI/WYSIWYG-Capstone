# Module detail:
# This file describes the Channel GUI class
# Objects of such class have the following attributes:
# This file also contains the tests for the Block module
class Channel:
	def __init__(self,source,destination,id,w,h,x=0,y=0):
		self.Source=source
		self.Destination=destination
		self.ID=id
	def changeSource(self,source):
		self.Source=source
	def changeDestination(self,destination):
		self.Destination=destination
