###################################
# CODE AUTHOR: GEORGE SKOUROUPATHIS
###################################
import databaseOperations
import re
import hashlib

def checkLogin(username, password):
	if (username, password) == (None, None):
		return "Username and Password were left empty"
	elif username == None:
		return "Username was left empty"
	elif password == None:
		return "Password was left empty"
	else:
		hashedPwd = hashlib.sha512(password).hexdigest()
		return databaseOperations.checkLogin(username, hashedPwd)
		
def checkRegister(email, username, password):

	if email == None or username == None or password == None:
		return "All the details marked with a * must be filled"
	elif not checkEmail(email):
		return "Email address is not valid"
	else:
		return databaseOperations.checkRegister(email, username)
		
def checkEmail(email):
	pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._%+-]+(\.\w)+$'
	return re.match(pattern, email)
	
def checkChangePassword(username, cpassword, npassword, rnpassword):
	if cpassword == None or npassword == None or rnpassword == None:
		return "Some of the fields were left blank"
	elif not databaseOperations.login(username, hashlib.sha512(cpassword).hexdigest()):
		return "Wrong current password entered"
	elif npassword != rnpassword:
		return "The new password was not repeated correctly"
	else:
		return None
	
def checkSendMessage(name, message):
	if name == None and message == None:
		return "Name and message left were left empty"
	if name == None:
		return "Name was left empty"
	if message == None:
		return "Message was left empty"
	else:
		return None
