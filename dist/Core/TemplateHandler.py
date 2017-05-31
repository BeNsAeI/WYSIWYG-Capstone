#!/usr/bin/python
from projectPath import projectPath
class fileIO:
	def __init__(self, fileType,p="Output.py"):
		self.fileType = fileType;
		self.extractedTempCode = '';
		self.pathName = '../Templates';
		self.extention = '.template.py';
		self.Path=p

	def read_fil(self,name):
		data = ''
		with open(self.pathName+"/"+name+self.extention, 'r') as myfile:
			data =data+ myfile.read().replace('\n', '\n')
		return data;

	def writefil(self,outstring,p="Output.py"):
		with open(p, 'w') as myfile:
			myfile.write(outstring)
		myfile.close()

if __name__ == '__main__':
    temp = fileIO("testCase");
    print(temp.read_fil("for"));
