#!/usr/bin/python

class fileIO:
	def __init__(self, fileType):
		self.fileType = fileType;
		self.extractedTempCode = '';
		self.pathName = '../Templates';
		self.extention = '.template.py';

	def read_fil(self,name):
		data = ''
		with open(self.pathName+"/"+name+self.extention, 'r') as myfile:
			data =data+ myfile.read().replace('\n', '\n')
		return data;

	def writefil(self):
		with open(self.pathName+"/"+name+self.extention, 'w') as myfile:
			myfile.write().replace('\n', '\n')
		return data;

if __name__ == '__main__':
    temp = fileIO("testCase");
    print(temp.read_fil("for"));
