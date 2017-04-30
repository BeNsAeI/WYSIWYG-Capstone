# This file is to generate the scope table and channel paths

class ParsingTable:
	def __init__(self):
		self.__Table = []
	def addChannel(self, channelStack):
		self.__Table = list(channelStack);
	def printTable(self):
		for i in self.__Table:
			print("Source:" + i.SourceID.Type + ", Destination: " + i.DestinationID.Type);

