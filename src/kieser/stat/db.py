__all__ = "connect", "schema"

from sqlobject import *
from sqlobject.sqlbuilder import JOIN, INNERJOINOn

def connect(*configfiles):
	from os import sep, environ
	from os.path import expanduser
	
	if not configfiles:
		configfiles = [
			"/etc/kieser/stat/db.ini",
			expanduser("~/.kieser/stat/db.ini"),
			 "kieser.stat.db.ini",
		]
		if "KIESER_STAT_DB_INI" in environ:
			configfiles.append(environ["KIESER_STAT_DB_INI"])
	
	from ConfigParser import SafeConfigParser
	config = SafeConfigParser(
		dict(
			database="mysql",
			user="", password="",
			host="localhost", port="3306",
			schema="dbgym",
			debug="no",
		)
	)
	config.read(configfiles)
	
	if config.has_section("connection"):
		opts = dict(
			(n,config.get("connection",n))
				for n in config.options("connection")
		)
		uri = \
			"%(database)s://%(user)s:%(password)s@" \
			"%(host)s:%(port)s/%(schema)s" % opts
		
		if config.getboolean("connection", "debug"):
			uri += "?debug=yes"
		
		from sqlobject import connectionForURI
		return connectionForURI(uri)

def schema(connection=None, prefix="", registry=None):
	
	if connection is None:
		connection = connect()
	
	if prefix is None:
		prefix = ""
	
	if registry is None:
		reg = str(id(connection))
	else:
		reg = registry 
	
	class Schema(object):
		
		class User(SQLObject):
			_connection = connection
			class sqlmeta:
				table = prefix + "users"
				fromDatabase = True
				registry = reg
			
			userID = UnicodeCol(notNone=True, alternateID=True, unique=True)
			surname = UnicodeCol(default=None)
			firstName = UnicodeCol(default=None)
			
			userMachines = MultipleJoin('UserMachine', joinColumn='user_id')
			sessions = MultipleJoin('Session', joinColumn='user_id') # orderBy='started' DOES NOT WORK!
			
			@property
			def lastSession(self):
				cls = self.__class__
				Session = classregistry.registry(cls.sqlmeta.registry).getClass('Session')
				select = Session.select(
					Session.q.userID==self.id,
					orderBy='-started',
				)[:1]
				results = tuple(select)
				if len(results) == 0:
					return None
				else:
					return results[0]
			
			@classmethod
			def byUserIDOrCreate(cls, userID):
				try:
					return cls.byUserID(userID)
				except SQLObjectNotFound:
					return cls(userID=userID)
			
			@classmethod
			def bySurname(cls, surname):
				return cls.select(cls.q.surname == surname)
			
			@classmethod
			def byFirstname(cls, first_name):
				return cls.select(cls.q.firstName == first_name)
			
		# End User
		
		class Machine(SQLObject):
			_connection = connection
			class sqlmeta:
				table = prefix + "machines"
				fromDatabase = True
				registry = reg
			
			name = UnicodeCol(notNone=True, alternateID=True, unique=True)
			description = UnicodeCol(notNone=True)
			
			userMachines = MultipleJoin('UserMachine', joinColumn='machine_id')
			
		# End Machine
		
		class UserMachine(SQLObject):
			_connection = connection
			class sqlmeta:
				table = prefix + "user_machines"
				fromDatabase = True
				registry = reg
			
			settings = UnicodeCol(default=None)
			
			user = ForeignKey('User')
			machine = ForeignKey('Machine')
			results = MultipleJoin('SessionResult', joinColumn='user_machine_id')
		
		# End UserMachine
		
		class Session(SQLObject):
			_connection = connection
			class sqlmeta:
				table = prefix + "sessions"
				fromDatabase = True
				registry = reg
			
			notes = UnicodeCol(default=None)
			
			user = ForeignKey('User')
			results = MultipleJoin('SessionResult', joinColumn='session_id')
		
		# End Session
		
		class SessionResult(SQLObject):
			_connection = connection
			class sqlmeta:
				table = prefix + "session_results"
				fromDatabase = True
				registry = reg
			
			session = ForeignKey('Session')
			userMachine = ForeignKey('UserMachine')
		
		# End SessionResult
		
	return Schema 

# End
