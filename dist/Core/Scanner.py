# This core file has the task of reading the screenand turning it into computer readale data
# It includes the tokens for tokenizing the data
# the toke is the only publicly available variable


class Token:
	def __init__(self,id,type,name,cid,cfid,ctid,comment):
		self.ID = id;
		self.type = type;
		self.name = name;
		self.channelID = cid;
		self.channelFromID = cfid;
		self.channelToID = ctid;
		self.comment = comment;

class Scanner:
	def __init__(self,total):
		self.__Tokens = [];
		self.__index = 0;
	def getTokens(blocks):
		while(True):
			handle = __getNextHandle(blocks[self.__index]);
			if(handle[0] == -1):
				print("The block \""+handle[2]+"\" is of unknown type!");
			if(handle[7]):
				tempToken = Token(handle[0],handle[1],handle[2],handle[3],handle[4],handle[5],handle[6]);
				self.__Tokens.append(tempToken);
			else:
				break;
		return self.__Tokens;
	def __getNextHandle(block):
		self.__index += 1;
		out = [];
		# ID [0]
		out.append(block.ID)
		# Type [1]
		out.append(block.type)
		# Name [2]
		out.append(block.Name)
		# Channel ID [3]
		out.append(block.)
		# Channel from ID [4]
		out.append(block.)
		# Channel to ID' [5]
		out.append(block.)
		# comment [6]
		out.append(block.)
		# is Valid Bool [7]
		out.append(1)
		return out;
