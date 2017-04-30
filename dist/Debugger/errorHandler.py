# This function grabs the error, output and string from command line while the code is running
import subprocess
import sys
'''def run(*popenargs, input=none, check = False, **kwargs):
	if input is not None:
		if 'stdin' in kwargs:
			raise ValueError('stdin and input arguments may not both be used.')
		kwargs['stdin'] = subprocess.PIPE

	process = subprocess.Popen(*popenargs, **kwargs):
	try:
		stdout, stderr = process.communicate(input)
	except:
		process.kill()
		process.wait()
		raise
	retcode = process.poll()
	if check and retcode:
		raise subprocess.CalledProcessError(
			retcode, process.args, output=stdout, stderr=stderr)
	return retcode, stdout, stderr
'''
class errorHandler:
	def __init__(self,o,f=''):
		self.command = "python "+o
		self.flag = f
		result = "No results"
		self.err = "No errors"
	def Monitor(self):
		print("Command: "+self.command+" "+self.flag)
		p = subprocess.Popen([self.command, self.flag], stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
		self.result, self.err = p.communicate()
	def makeReport(self):
		print("Result: ")
		print(self.result)
		print("Error: ")
		print(self.err)
	def logToFile(self):
		pass
def testcase():
	temp = errorHandler("Output.py")
	temp.Monitor()
	temp.makeReport()
testcase()
