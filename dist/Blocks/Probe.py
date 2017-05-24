# Module detail:
# This file describes the Probe GUI class
# Objects of such class have the following attributes:
# This file also contains the tests for the Block module
class Probe:
	def __init__(self):
		self.text = ""
		self.channelID = None
	def Display(var):
		self.text = str(var)
	def inject(probes,id):
		tmpText = "print(\"Probe["+str(id)+"]: "+probes[id]+"\")\n"
		return tmpText
