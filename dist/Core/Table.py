# This file is to generate the scope table and channel paths

class ParsingTable:
	def __init__(self):
		self.__Table = []
	def addChannel(self, channelStack):
		self.__Table = list(channelStack);

