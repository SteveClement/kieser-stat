import db
from datetime import datetime, date, time, timedelta
from sqlobject import AND, OR, LIKE, SQLObjectNotFound

now, today = datetime.now, date.today

connection = db.connect()
schema = db.schema(connection)
#connection.debug = True

User = schema.User
Machine = schema.Machine
UserMachine = schema.UserMachine
Session = schema.Session
SessionResult = schema.SessionResult

# Useful classes

class Counter(object):
	def __init__(self, start=1):
		from itertools import count
		self.counter = count(start)
	def next(self): return self.counter.next()
	count = property(next)

# End
