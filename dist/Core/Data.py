# This file contains a module for connecting to database
# it could be included included in differrent core files for data reading and book keeping purposes
# mySQL and This also generates local files
import MySQLdb
class DataPy:
	def DB(self,op):
		import MySQLdb
		# Open database connection
		db = MySQLdb.connect("localhost","admin","1234","WYSIWYG" )
		# prepare a cursor object using cursor() method
		cursor = db.cursor()
		# execute SQL query using execute() method.
		cursor.execute("SELECT VERSION()")
		# Fetch a single row using fetchone() method.
		data = cursor.fetchone()
		print "Database version : %s " % data

		#write
#		if(op):
			
		#read
#		else:
			
		#disconnecting from the server
		db.close()
#	def Local(self,op):
		#write
#		if (op):

		#read
#		else:

#	def Write():

#	def Read();

def testCase():
	save = DataPy();
	save.DB(True);
testCase()
