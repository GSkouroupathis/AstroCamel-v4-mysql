###################################
# CODE AUTHOR: GEORGE SKOUROUPATHIS
###################################
import os
import MySQLdb

#Connect to a database. Create it if it doesn't exist
def connectToDatabase(database):
	global dbConnection
	global dbCursor

	dbConnection = MySQLdb.connect('localhost', 'root', 'w3lcome', database)
	dbCursor = dbConnection.cursor()
	
	if not dbConnection:
		print 'Connection to database', database, 'failed'
		return

	if not dbCursor:
		print 'Setting the cursor of database', database, 'failed'
		return

#Close the connection to a database.
def closeConnectionToDatabase():
	dbCursor.close()
	dbConnection.close()
		
#Initializes all the tables in the database
def initTables():
	global dbCursor
	
	#Drop tables in case they already exist
	try:
		dbCursor.execute('DROP TABLE users_table')
	except:
		pass
		
	try:
		dbCursor.execute('DROP TABLE content_table')
	except:
		pass
			
	try:
		dbCursor.execute('DROP TABLE comments_table')
	except:
		pass
	
	try:
		dbCursor.execute('DROP TABLE news_table')
	except:
		pass
		
	try:
		dbCursor.execute('DROP TABLE code_table')
	except:
		pass
		
	try:
		dbCursor.execute('DROP TABLE art_table')
	except:
		pass
		
	try:
		dbCursor.execute('DROP TABLE msgs_table')
	except:
		pass

	######################### users_table #########################
	dbCursor.execute('''CREATE TABLE users_table (
			user_id INT,
			email VARCHAR(50),
			username VARCHAR(20),
			password VARCHAR(128),
			ip_address VARCHAR(15),
			verified INT DEFAULT 0,
			admin INT DEFAULT 0,
			banned INT DEFAULT 0,
			resetCode VARCHAR(15) DEFAULT 'aaaaaaaaaaaaaaa',
			PRIMARY KEY (user_id),
			UNIQUE (email)
			)''')
			
	dbCursor.execute('''INSERT INTO users_table
		VALUES (1, 'george_skouroupathis@hotmail.com', 'admin',
		'c7ad44cbad762a5da0a452f9e854fdc1e0e7a52a38015f23f3eab1d80b931dd472634dfac71cd34ebc35d16ab7fb8a90c81f975113d6c7538dc69dd8de9077ec',
		'1337.1337', 1, 1, 0, 'V0e_aaaaaaa5FmU')
		''')

	dbCursor.execute('''INSERT INTO users_table
		VALUES (2, 'admin@astrocamel.com', 'administrator',
		'cf835de3d4ea01367c45e412e7a9393a85a4e40af149ed8c3ed6c37c05b67b27813d7ff8072c1035cedd19415adf17128d63186f05f0d656002b0ca1c34f44a0',
		'1337.1337', 1, 1, 0, '*e8QaaaaaaanYNf')
		''')

	######################### content_table #########################
	dbCursor.execute('''CREATE TABLE content_table (
			content_id INT,
			content_type VARCHAR(4),
			PRIMARY KEY (content_id),
			CHECK (content_type IN ("news", "code", "art"))
			)''')
	
	dbCursor.execute('''INSERT INTO content_table
		VALUES (1, 'news')
		''')
	
	dbCursor.execute('''INSERT INTO content_table
		VALUES (2, 'code')
		''')
	
	dbCursor.execute('''INSERT INTO content_table
		VALUES (3, 'code')
		''')
	
	dbCursor.execute('''INSERT INTO content_table
		VALUES (4, 'code')
		''')
	
	dbCursor.execute('''INSERT INTO content_table
		VALUES (5, 'code')
		''')
	
	dbCursor.execute('''INSERT INTO content_table
		VALUES (6, 'code')
		''')
	
	dbCursor.execute('''INSERT INTO content_table
		VALUES (7, 'code')
		''')
	
	dbCursor.execute('''INSERT INTO content_table
		VALUES (8, 'code')
		''')
	
	dbCursor.execute('''INSERT INTO content_table
		VALUES (9, 'code')
		''')
	
	dbCursor.execute('''INSERT INTO content_table
		VALUES (10, 'code')
		''')
	
	dbCursor.execute('''INSERT INTO content_table
		VALUES (11, 'code')
		''')
	
	dbCursor.execute('''INSERT INTO content_table
		VALUES (12, 'art')
		''')
	
	dbCursor.execute('''INSERT INTO content_table
		VALUES (13, 'art')
		''')
	
	dbCursor.execute('''INSERT INTO content_table
		VALUES (14, 'art')
		''')
	
	dbCursor.execute('''INSERT INTO content_table
		VALUES (15, 'art')
		''')
	
	dbCursor.execute('''INSERT INTO content_table
		VALUES (16, 'art')
		''')
	
	dbCursor.execute('''INSERT INTO content_table
		VALUES (17, 'art')
		''')
	
	dbCursor.execute('''INSERT INTO content_table
		VALUES (18, 'art')
		''')
	
	dbCursor.execute('''INSERT INTO content_table
		VALUES (19, 'art')
		''')
	
	dbCursor.execute('''INSERT INTO content_table
		VALUES (20, 'art')
		''')
	
	dbCursor.execute('''INSERT INTO content_table
		VALUES (21, 'art')
		''')
	
	dbCursor.execute('''INSERT INTO content_table
		VALUES (22, 'art')
		''')
	
	dbCursor.execute('''INSERT INTO content_table
		VALUES (23, 'art')
		''')
	
	dbCursor.execute('''INSERT INTO content_table
		VALUES (24, 'art')
		''')
	
	dbCursor.execute('''INSERT INTO content_table
		VALUES (25, 'art')
		''')
	
	dbCursor.execute('''INSERT INTO content_table
		VALUES (26, 'art')
		''')
	
	dbCursor.execute('''INSERT INTO content_table
		VALUES (27, 'art')
		''')
	
	dbCursor.execute('''INSERT INTO content_table
		VALUES (28, 'art')
		''')
	
	dbCursor.execute('''INSERT INTO content_table
		VALUES (29, 'art')
		''')
	
	dbCursor.execute('''INSERT INTO content_table
		VALUES (30, 'art')
		''')
	
	dbCursor.execute('''INSERT INTO content_table
		VALUES (31, 'art')
		''')
	
	dbCursor.execute('''INSERT INTO content_table
		VALUES (32, 'art')
		''')
	
	dbCursor.execute('''INSERT INTO content_table
		VALUES (33, 'art')
		''')
	
	dbCursor.execute('''INSERT INTO content_table
		VALUES (34, 'art')
		''')
	
	dbCursor.execute('''INSERT INTO content_table
		VALUES (35, 'art')
		''')
	######################### comments_table #########################
	dbCursor.execute('''CREATE TABLE comments_table (
			comment_id INT,
			content_id INT,
			user_id INT,
			comment VARCHAR(255),
			date TEXT(20),
			PRIMARY KEY (comment_id),
			FOREIGN KEY (content_id) REFERENCES content_table (content_id)
				ON UPDATE CASCADE ON DELETE CASCADE,
			FOREIGN KEY (user_id) REFERENCES users_table (user_id)
				ON UPDATE CASCADE ON DELETE CASCADE
			)''')
	
	dbCursor.execute('''INSERT INTO comments_table
		VALUES  (1, 1, 1, 'Welcome to the site!', '31 Aug 1337 18:59')
		''')
		
	######################### news_table #########################
	dbCursor.execute('''CREATE TABLE news_table (
			news_id INTEGER,
			content_id INT,
			title VARCHAR(100),
			date TEXT(20),
			PRIMARY KEY (news_id),
			FOREIGN KEY (content_id) REFERENCES content_table (content_id)
				ON UPDATE CASCADE ON DELETE CASCADE
			)''')

	dbCursor.execute('''INSERT INTO news_table
		VALUES  (1, 1, 'Welcome to the site!', '31 Aug 1337 18:58')
		''')

	######################### code_table #########################
	dbCursor.execute('''CREATE TABLE code_table (
			code_id INT,
			content_id INT,
			title VARCHAR(100),
			code_type TEXT(15),
			description VARCHAR(250),
			PRIMARY KEY (code_id),
			FOREIGN KEY (content_id) REFERENCES content_table (content_id)
				ON UPDATE CASCADE ON DELETE CASCADE
			)''')

	
	dbCursor.execute('''INSERT INTO code_table
		VALUES  (1, 5, 'Encoder #2', 'php', ' Uses polyalphabetic substitution to encode your plaintext into a more complex cipher')
		''')
		
	dbCursor.execute('''INSERT INTO code_table
		VALUES  (2, 6, 'Encoder #1', 'php', ' Uses monoalphabetic substitution to encode your plaintext into a simple cipher')
		''')	
		
	dbCursor.execute('''INSERT INTO code_table
		VALUES  (3, 7, 'Page Hit Counter', 'php', 'Counts how many visits a webpage has had')
		''')
		
	dbCursor.execute('''INSERT INTO code_table
		VALUES  (4, 8, 'MD5 Brute Forcer', 'php', 'Takes an MD5 hash in hexadecimal form and brute forces it to find the password')
		''')
		
	dbCursor.execute('''INSERT INTO code_table
		VALUES  (5, 9, 'Login Script', 'php', 'Allows you to authenticate to another page. Username is "admin" and password is "enterthecamel"')
		''')
			
	dbCursor.execute('''INSERT INTO code_table
		VALUES  (6, 10, 'Socket Client', 'python', 'Sets up a communication between the server and the client. The client side sends messages')
		''')
		
	dbCursor.execute('''INSERT INTO code_table
		VALUES  (7, 11, 'Socket Server', 'python', 'Sets up a communication between the server and the client. The server side receives messages')
		''')
		
	dbCursor.execute('''INSERT INTO code_table
		VALUES  (8, 12, 'Real 6 Solver', 'python', 'Solves HackThisSite realistic challenge #6 (www.hackthissite.org/playlevel/6/)')
		''')	
				
	dbCursor.execute('''INSERT INTO code_table
		VALUES  (9, 13, 'Prog 1 Solver', 'python', 'Solves HackThisSites programming challenge #1 (www.hackthissite.org/missions/prog/1/)')
		''')		
			
	dbCursor.execute('''INSERT INTO code_table
		VALUES  (10, 14, 'Triangular Encryption', 'python', 'Encrypts the plaintext using the triangle algorithm')
		''')
	
	######################### art_table #########################
	dbCursor.execute('''CREATE TABLE art_table (
			art_id INT,
			content_id INT,
			description VARCHAR(200),
			art_type TEXT(15),
			PRIMARY KEY (art_id),
			FOREIGN KEY (content_id) REFERENCES content_table (content_id)
				ON UPDATE CASCADE ON DELETE CASCADE
			)''')
	
	dbCursor.execute('''INSERT INTO art_table
		VALUES  (1, 15, 'Forgotten Garden', 'website')
		''')
	
	dbCursor.execute('''INSERT INTO art_table
		VALUES  (2, 16, 'City Skyline Theme', 'website')
		''')
	
	dbCursor.execute('''INSERT INTO art_table
		VALUES  (3, 17, 'Blue Ground 9! Full of computing challenges', 'website')
		''')
	
	dbCursor.execute('''INSERT INTO art_table
		VALUES  (4, 18, 'Red Theme using JQuery', 'website')
		''')
	
	dbCursor.execute('''INSERT INTO art_table
		VALUES  (5, 19, 'The second version of Astrocamel.com!', 'website')
		''')
	
	dbCursor.execute('''INSERT INTO art_table
		VALUES  (6, 20, 'An urban themed website', 'website')
		''')
	
	dbCursor.execute('''INSERT INTO art_table
		VALUES  (7, 21, 'ToPloumi.com - A website I created for the woodcarving bussiness', 'website')
		''')
	
	dbCursor.execute('''INSERT INTO art_table
		VALUES  (8, 22, 'Quantum Logic - A website I created for an assignment', 'website')
		''')
	
	dbCursor.execute('''INSERT INTO art_table
		VALUES  (9, 23, 'Vincent - Design with opacity', 'website')
		''')
	
	dbCursor.execute('''INSERT INTO art_table
		VALUES  (10, 24, 'The third version of Astrocamel.com!', 'website')
		''')
	
	dbCursor.execute('''INSERT INTO art_table
		VALUES  (11, 25, 'Kenny, Cartman, Stan, Kyle', 'gfx')
		''')

	dbCursor.execute('''INSERT INTO art_table
		VALUES  (12, 26, 'Ironman MARK I', 'gfx')
		''')

	dbCursor.execute('''INSERT INTO art_table
		VALUES  (13, 27, 'Three Days of the Condor', 'gfx')
		''')

	dbCursor.execute('''INSERT INTO art_table
		VALUES  (14, 28, 'HackThisZine Cover', 'gfx')
		''')

	dbCursor.execute('''INSERT INTO art_table
		VALUES  (15, 29, 'Freedom', 'gfx')
		''')

	dbCursor.execute('''INSERT INTO art_table
		VALUES  (16, 30, 'Dead Flower', 'gfx')
		''')

	dbCursor.execute('''INSERT INTO art_table
		VALUES  (17, 31, 'Bicommunal Rock Concert flyer', 'gfx')
		''')

	dbCursor.execute('''INSERT INTO art_table
		VALUES  (18, 32, 'The Call of Cthulhu', 'gfx')
		''')

	dbCursor.execute('''INSERT INTO art_table
		VALUES  (19, 33, 'Orange', 'gfx')
		''')

	dbCursor.execute('''INSERT INTO art_table
		VALUES  (20, 34, 'Generic Album Cover', 'gfx')
		''')

	dbCursor.execute('''INSERT INTO art_table
		VALUES  (21, 35, 'The Millenium Falcon', 'gfx')
		''')
		
	######################### msgs_table #########################
	dbCursor.execute('''CREATE TABLE msgs_table (
			msg_id INT,
			name VARCHAR(30),
			content VARCHAR(255),
			date TEXT(20),
			ip_address VARCHAR(15),
			PRIMARY KEY (msg_id)
			)''')
	
	dbCursor.execute('''INSERT INTO msgs_table
		VALUES  (1, "gs512", "This is a nice message", '30 Aug 2012 18:59', "21.26.20.3")
		''')

	dbConnection.commit()

#Returns a list with the users
def fetchAllUsers():
	global dbCursor
	
	dbCursor.execute('SELECT * FROM users_table ORDER BY username ASC')
	return dbCursor.fetchall()
	
#Returns a list with the news
def fetchAllNews(n):
	global dbCursor
	
	SQL = ('SELECT * FROM news_table ORDER BY news_id DESC limit %s')
	data = (n,)
	dbCursor.execute(SQL, data)
	return dbCursor.fetchall()

def fetchCodes(n):
	global dbCursor
	
	#dbCursor.execute('SELECT * FROM code_table ORDER BY code_id DESC LIMIT %d' %n)
	dbCursor.execute('SELECT * FROM code_table ORDER BY code_id DESC')
	return dbCursor.fetchall()

def fetchArts(n):
	global dbCursor
	
	#dbCursor.execute('SELECT * FROM art_table ORDER BY art_id DESC LIMIT %d' %n)
	dbCursor.execute('SELECT * FROM art_table ORDER BY art_id DESC')
	return dbCursor.fetchall()

def fetchGfxs(n):
	global dbCursor
	
	dbCursor.execute('SELECT * FROM art_table WHERE art_type="gfx" ORDER BY art_id DESC')
	return dbCursor.fetchall()

def fetchWebs(n):
	global dbCursor
	
	dbCursor.execute('SELECT * FROM art_table WHERE art_type="website" ORDER BY art_id DESC')
	return dbCursor.fetchall()

def fetchMsgs(n):
	global dbCursor
	
	dbCursor.execute('SELECT * FROM msgs_table ORDER BY msg_id DESC')
	return dbCursor.fetchall()

#login is only used in checkLogin and changePassword
def login(username, hashedPwd):
	global dbCursor
	
	#trick to return number of records
	SQL = 'SELECT * FROM users_table WHERE username=%s AND password=%s'
	data = (username, hashedPwd)
	return dbCursor.execute(SQL, data)

def checkLogin(username, hashedPwd):
	global dbCursor
	
	if login(username, hashedPwd) == 0:
		return "Wrong username/password compination"
	elif not isVerified(username):
		return "Username " + username + " is not verified"
	elif isBanned(username):
		return "Username " + username + " is banned"
	else:
		return None
		
def register(email, username, hashedPwd, ip_address):
	global dbCursor
	
	dbCursor.execute('SELECT MAX(user_id) FROM users_table')
	nextUserId = dbCursor.fetchone()[0] + 1
	
	SQL = 'INSERT INTO users_table(user_id, email, username, password, ip_address) \
		VALUES(%s, %s, %s, %s, %s)'
	data = (nextUserId, email, username, hashedPwd, ip_address)	
	dbCursor.execute(SQL, data)
	dbConnection.commit()

def checkRegister(email, username):
	global dbCursor

	SQL = 'SELECT * FROM users_table WHERE email=%s AND username=%s'
	data = (email, username)
	regRes = dbCursor.execute(SQL, data)
	if regRes != 0:
		return "This email and username are already in use"

	SQL = 'SELECT * FROM users_table WHERE email=%s'
	data = (email,)
	regRes = dbCursor.execute(SQL, data)
	if regRes != 0:
		return "This email is already in use"		
		
	SQL = 'SELECT * FROM users_table WHERE username=%s'
	data = (username,)
	regRes = dbCursor.execute(SQL, data)
	if regRes != 0:
		return "This username is already in use"
	
	return None

##VERIFIED, ADMIN, BANNED TESTS####################################################
def isVerified(username):
	global dbCursor
	
	SQL = 'SELECT * FROM users_table WHERE username=%s AND verified=1'
	data = (username,)
	verRes = dbCursor.execute(SQL, data)
	if verRes == 1:
		return True
	else:
		return False

def verify(username):
	global dbCursor
	
	SQL = 'UPDATE users_table SET verified=1 WHERE username=%s'
	data = (username,)
	dbCursor.execute(SQL, data)
	dbConnection.commit()
			
def isAdmin(username):
	global dbCursor
	
	SQL = 'SELECT * FROM users_table WHERE username=%s AND admin=1'
	data = (username,)
	dbCursor.execute(SQL, data)
	if len( dbCursor.fetchall() ) == 1:
		return True
	else:
		return False

def giveAdmin(username):
	global dbCursor
	
	SQL = 'UPDATE users_table SET admin=1 WHERE username=%s'
	data = (username,)
	dbCursor.execute(SQL, data)
	dbConnection.commit()

def removeAdmin(username):
	global dbCursor
	
	SQL = 'UPDATE users_table SET admin=0 WHERE username=%s'
	data = (username,)
	dbCursor.execute(SQL, data)
	dbConnection.commit()
	
def isBanned(username):
	global dbCursor
	
	SQL = 'SELECT * FROM users_table WHERE username=%s AND banned=1'
	data = (username,)
	banRes = dbCursor.execute(SQL, data)
	if banRes == 1:
		return True
	else:
		return False

def ban(username):
	global dbCursor
	
	SQL = 'UPDATE users_table SET banned=1 WHERE username=%s'
	data = (username,)
	dbCursor.execute(SQL, data)
	dbConnection.commit()

def unban(username):
	global dbCursor
	
	SQL = 'UPDATE users_table SET banned=0 WHERE username=%s'
	data =  (username,)
	dbCursor.execute(SQL, data)
	dbConnection.commit()	
###################################################################################
	
def getIDFromUser(username):
	global dbCursor
	
	SQL = 'SELECT user_id FROM users_table WHERE username=%s'
	data = (username,)
	dbCursor.execute(SQL, data)
	return dbCursor.fetchone()

def getPasswordFromUser(username):
	global dbCursor
	
	SQL = 'SELECT password FROM users_table WHERE username=%s'
	data =  (username,)
	dbCursor.execute(SQL, data)
	return dbCursor.fetchone()
	
def getContentTypeFromID(content_id):
	global dbCursor
	
	SQL = 'SELECT content_type FROM content_table WHERE content_id=%s'
	data = (content_id,)
	dbCursor.execute(SQL, data)
	return dbCursor.fetchone()
	
def getContentIDFromCommentID(comment_id):
	global dbCursor
	
	SQL = 'SELECT content_id FROM comments_table WHERE comment_id=%s'
	data = (comment_id,)
	dbCursor.execute(SQL, data)
	return dbCursor.fetchone()
	
def getUserFromCommentID(comment_id):
	global dbCursor
	
	SQL = 'SELECT username FROM comments_table NATURAL JOIN users_table WHERE comment_id=%s'
	data = (comment_id,)
	dbCursor.execute(SQL, data)
	return dbCursor.fetchone()
	
def getContentIDFromArtID(art_id):
	global dbCursor
	
	SQL = 'SELECT content_id FROM art_table WHERE art_id=%s'
	data = (art_id,)
	dbCursor.execute(SQL, data)
	return dbCursor.fetchone()
	
def getEmailFromUsername(username):
	global dbCursor
	
	SQL = 'SELECT email FROM users_table WHERE username=%s'
	data = (username,)
	dbCursor.execute(SQL, data)
	return dbCursor.fetchone()
	
def getResetCodeFromUsername(username):
	global dbCursor
	
	SQL = 'SELECT resetCode FROM users_table WHERE username=%s'
	data = (username,)
	dbCursor.execute(SQL, data)
	return dbCursor.fetchone()
	
def ResetPassword(username, hashedPwd):
	global dbCursor
	
	SQL = 'UPDATE users_table SET password=%s WHERE username=%s'
	data = (hashedPwd, username)
	dbCursor.execute(SQL, data)
	dbConnection.commit()	
	
def insertNews(title, date):
	global dbCursor
	
	dbCursor.execute('SELECT MAX(content_id) FROM content_table')
	nextContentId = dbCursor.fetchone()[0] + 1
	SQL = '''INSERT INTO content_table
		VALUES (%s, 'news')'''
	data = (nextContentId,)
	dbCursor.execute(SQL, data)
	
	dbCursor.execute('SELECT MAX(news_id) FROM news_table')
	nextNewsId = dbCursor.fetchone()[0] + 1
	SQL = '''INSERT INTO news_table
		VALUES (%s, %s, %s, %s)'''
	data = (nextNewsId, nextContentId, title, date)
	dbCursor.execute(SQL, data)
	dbConnection.commit()

def insertCode(title, code_type, description):
	global dbCursor
	
	dbCursor.execute('SELECT MAX(content_id) FROM content_table')
	nextContentId = dbCursor.fetchone()[0] + 1
	SQL = '''INSERT INTO content_table
		VALUES (%s, 'code')'''
	data = (nextContentId,)
	dbCursor.execute(SQL, data)
	
	dbCursor.execute('SELECT MAX(code_id) FROM code_table')
	nextCodeId = dbCursor.fetchone()[0] + 1
	SQL = '''INSERT INTO code_table
		VALUES (%s, %s, %s, %s, %s)'''
	data = (nextCodeId, nextContentId, title, code_type, description)	
	dbCursor.execute(SQL, data)
	dbConnection.commit()

def insertGfx(description):
	global dbCursor
	
	dbCursor.execute('SELECT MAX(content_id) FROM content_table')
	nextContentId = dbCursor.fetchone()[0] + 1
	SQL = '''INSERT INTO content_table
		VALUES (%s, 'art')'''
	data = (nextContentId,)
	dbCursor.execute(SQL, data)
	
	dbCursor.execute('SELECT MAX(art_id) FROM art_table')
	nextArtId = dbCursor.fetchone()[0] + 1
	SQL = '''INSERT INTO art_table
		VALUES (%s, %s, %s, 'gfx')'''
	data = (nextContentId, nextArtId, description)
	dbCursor.execute(SQL, data)	
	dbConnection.commit()
	
def insertComment(content_id, user_id, comment, date):
	global dbCursor
	
	dbCursor.execute('SELECT MAX(comment_id) FROM comments_table')
	nextCommentId = dbCursor.fetchone()[0] + 1
	SQL = '''INSERT INTO comments_table
		VALUES (%s, %s, %s, %s, %s)'''
	data = (nextCommentId, content_id, user_id, comment, date)
	dbCursor.execute(SQL, data)
	dbConnection.commit()

def insertMessage(name, message, date, ip_addess):
	global dbCursor
	
	dbCursor.execute('SELECT MAX(msg_id) FROM msgs_table')
	nextMsgId = dbCursor.fetchone()[0] + 1
	SQL = '''INSERT INTO msgs_table
		VALUES (%s, %s, %s, %s, %s)'''
	data = (nextMsgId, name, message, date, ip_addess)
	dbCursor.execute(SQL, data)
	dbConnection.commit()
	
def deleteComment(comment_id):
	global dbCursor
	
	SQL = 'DELETE FROM comments_table WHERE comment_id=%s'
	data = (comment_id,)
	dbCursor.execute(SQL, data)
	dbConnection.commit()

def deleteNews(news_id):
	global dbCursor
	
	SQL = 'DELETE FROM news_table WHERE news_id=%s'
	data =  (news_id,)
	dbCursor.execute(SQL, data)
	dbConnection.commit()
	
def fetchNews(content_id):
	global dbCursor
	
	SQL = 'SELECT * FROM news_table where content_id=%s'
	data = (content_id,)
	dbCursor.execute(SQL, data)
	return dbCursor.fetchone()
	
def fetchArt(content_id):
	global dbCursor
	
	SQL = 'SELECT * FROM art_table where content_id=%s'
	data = (content_id,)
	dbCursor.execute(SQL, data)
	return dbCursor.fetchone()
	
def fetchCode(content_id):
	global dbCursor
	
	SQL = 'SELECT * FROM code_table where content_id=%s'
	data = (content_id,)
	dbCursor.execute(SQL, data)
	return 	dbCursor.fetchone()

def fetchComments(content_id):
	global dbCursor
		
	SQL = 'SELECT comment_id, content_id, user_id, username, comment, date FROM comments_table NATURAL JOIN users_table WHERE content_id=%s ORDER BY comment_id DESC'
	data = (content_id,)
	dbCursor.execute(SQL, data)
	return dbCursor.fetchall()
	
def fetchCommentNum(content_id):
	global dbCursor

	SQL = 'SELECT count(*) FROM comments_table where content_id=%s'
	data = (content_id,)
	dbCursor.execute(SQL, data)
	return dbCursor.fetchone()
	
def getNextNewsID():
	global dbCursor
	
	dbCursor.execute('SELECT MAX(news_id) FROM news_table')	
	return dbCursor.fetchone()[0] + 1
	
def getNextCodeID():
	global dbCursor
	
	dbCursor.execute('SELECT MAX(code_id) FROM code_table')	
	return dbCursor.fetchone()[0] + 1

def getNextArtID():
	global dbCursor
	
	dbCursor.execute('SELECT MAX(art_id) FROM art_table')	
	return dbCursor.fetchone()[0] + 1
	
def changeResetCode(username, resetCode):
	global dbCursor
	
	SQL = 'UPDATE users_table SET resetCode=%s WHERE username=%s'
	data = (resetCode, username)
	dbCursor.execute(SQL, data)
	dbConnection.commit()
	
def changeEmailAddress(username, email):
	global dbCursor
	
	SQL = 'UPDATE users_table SET email=%s WHERE username=%s'
	data = (email, username)
	dbCursor.execute(SQL, data)
	dbConnection.commit()

def changePassword(username, hashedPwd):
	global dbCursor
	
	SQL = 'UPDATE users_table SET password=%s WHERE username=%s'
	data = (hashedPwd, username)
	dbCursor.execute(SQL, data)
	dbConnection.commit()
