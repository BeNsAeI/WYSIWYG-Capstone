#!/usr/bin/python

class fileIO:
	def __init__(self, fileType):
		self.fileType = fileType;
		self.extractedTempCode = '';
		self.pathName = '/TestFlder';

	def read_fil(self):
		with open(self.fileType+'.template', 'r') as myfile:
			data = myfile.read().replace('\n', '__/')
		return data;

	def writefil(self):
		with open(self.fileType+'.template', 'r') as myfile:
			myfile.write().replace('__/', '\n')
		return data;

if __name__ == '__main__':
    temp = fileIO("testCase");
    print(temp.read_fil());
