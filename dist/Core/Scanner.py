# This core file has the task of reading the screenand turning it into computer readale data
# It includes the tokens for tokenizing the data
# the toke is the only publicly available variable


class Token:
	def __init__(self,id,type,name,cid,cfid,ctid):
		self.ID = id;
		self.type = type;
		self.name = name;
		self.channelID = cid;
		self.channelFromID = cfid;
		self.channelToID = ctid;

class Scanner:
	def __init__(self,total):
		self.__Tokens = [];
		self.__index = 0;
	def getTokens():
		while(True):
			handle = __getNextHandle();
			if(handle[1] == -1):
				print("The block with ID " + + " is of unknown type!");
			if(handle[6]):
				tempToken = Token(handle[0],handle[1],handle[2],handle[3],handle[4],handle[5]);
				self.__Tokens.append(tempToken);
			else:
				break;
		return self.__Tokens;
	def __getNextHandle():
		out = [];
		#append ID
		if(False):
			#bad block type
			out.append(-1);
		else:
			# Type
		# Name
		# Channel ID
		# Channel from ID
		# Channel to ID'
		# bool is valid
		return out;
