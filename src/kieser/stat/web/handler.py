#!/usr/bin/env python

import kid, random, sys
from mod_python import apache
from mod_python.apache import OK, DECLINED
from mod_python import util
from mod_python.Session import Session as WebSession
from mod_python.Session import BaseSession
from kieser.stat.runtime import *
from sqlobject.sqlbuilder import JOIN, INNERJOINOn

import os
os.environ['MATPLOTLIBDATA'] = "/tmp"

kid.enable_import()

def load_user(obj):
	if isinstance(obj, BaseSession):
		userID = obj.get("userID", None)
	else:
		userID = obj
	
	if userID is None:
		return None
	
	try:
		return User.byUserID(userID)
	except SQLObjectNotFound:
		return None

def setup(func):
	def _setup(req):
		res = func(req)
		if res is None: res = OK
		raise apache.SERVER_RETURN, res 
	return _setup

def render(req, page, **kw):
	media_type, charset = 'text/html', 'utf-8'
	req.content_type = "%s;charset=%s" % (media_type, charset)
	write = req.write
	template = page.Template(
		this=req.base_uri, req=req, user=load_user(req.session), **kw
	)
	tgen = template.generate(encoding=charset, output="html-strict")
	for part in tgen: write(part)

def get_date(name, req):
	def get(n):
		return int(
			req.fields.getfirst(
				"%s-%s" % (name,n)
			)
		)
	return date(
		get('year'), get('month'), get('day'),
	)

def get_time(name, req):
	def get(n):
		return int(
			req.fields.getfirst(
				"%s-%s" % (name,n)
			)
		)
	return time(
		get('hour'), get('minute'),
	)

def get_datetime(name, req):
	def get(n):
		return int(
			req.fields.getfirst(
				"%s-%s" % (name,n)
			)
		)
	return datetime(
		get('year'), get('month'), get('day'),
		get('hour'), get('minute'),
	)

def get_duration(name, req):
	def get(n):
		return int(
			req.fields.getfirst(
				"%s-%s" % (name,n)
			)
		)
	hours, minutes = get('hours'), get('minutes')
	return "%02d:%02d" % (hours, minutes)

@setup
def index(req):
	user = load_user(req.session)
	if user is None:
		import login as page
	else:
		import home as page
	render(req, page)

@setup
def login(req):
	userID = req.fields.getfirst("userID", None)
	password = req.fields.getfirst("password", None)
	message = None
	
	if userID is None or password is None:
		import login as page
		render(
			req, page,
			message = "Incomplete credentials; "
				"please supply a user name and password",
		)
		return OK
	else:
		userID, password = userID.value, password.value
	
	# check user name and password
	user = load_user(userID)
	if user is None:
		import login as page
		render(
			req, page,
			message="User '%s' not found" % userID,
		)
		return OK
	else:
		req.session["userID"] = userID
	
	import home as page
	render(req, page)
# End login

@setup
def logout(req):
	req.session.invalidate()
	return index(req)
# End logout

@setup
def home(req):
	user = load_user(req.session)
	if user is None:
		import login as page
		render(req, page, goingto="home")
	else:
		import home as page
		render(req, page)
# End sessions

@setup
def sessions(req):
	user = load_user(req.session)
	
	if user is None:
		import login as page
		render(req, page, goingto="sessions")
	
	elif "new" in req.fields:
		# fetch the previous sessions immediately, because SQLObject selects
		# lazily, but inserts immediately. Grr.
		lastSession = user.lastSession
		session = Session(userID=user.id, started=now(), duration=0)
		if lastSession is not None:
			for result in lastSession.results:
				SessionResult(
					sessionID=session.id, userMachineID=result.userMachineID,
					duration=result.duration, loading=result.loading,
				)
		
		import session_edit as page
		render(req, page, session=session)
	
	elif "edit" in req.fields:
		edit = long(req.fields.getfirst("edit", ""))
		session = Session.get(edit)
		if session.user != user:
			raise "Session does not belong to you"
		
		import session_edit as page
		render(req, page, session=session)
	
	elif "update" in req.fields:
		messages = []
		update = long(req.fields.getfirst("update", ""))
		session = Session.get(update)
		if session.user != user:
			raise "Session does not belong to you"
		
		notes = req.fields.getfirst("notes", None)
		if notes is not None: notes = notes.value 
		session.notes = notes
		try:
			session.started = get_datetime('started', req)
		except ValueError, e:
			messages.append(unicode(e))
		
		# We need a string like '12:34' to set this field, yet SQLObject returns
		# a datetime.timedelta object when queried. But then, so the rest of our
		# code is okay we need to sync the object after the change. Borked!
		session.duration = get_duration('duration', req)
		session.sync()
		
		umids = tuple(long(umid)
			for umid in req.fields.getlist("userMachineID"))
		
		results = dict( (r.userMachine, r) for r in session.results )
		
		for umid in umids:
			um = UserMachine.get(umid)
			if um.user != user:
				raise "This machine is not yours!"
			
			loading, duration = "loading-%d" % umid, "duration-%d" % umid
			if loading in req.fields:
				loading = int(req.fields.getfirst(loading))
			else:
				loading = None
			if duration in req.fields:
				duration = int(req.fields.getfirst(duration))
			else:
				duration = None
			
			if loading is None and duration is None:
				if um in results:
					SessionResult.delete(results.pop(um).id)
			elif um in results:
				res = results[um]
				res.set(loading=loading, duration=duration)
			else:
				res = SessionResult(
					sessionID=session.id, userMachineID=um.id,
					duration=duration, loading=loading
				)
		
		if messages:
			import session_edit as page
			render(req, page, session=session, message=", ".join(messages))
		else:
			import sessions as page
			render(req, page)
	
	else:
		import sessions as page
		render(req, page)

# End sessions

@setup
def usermach(req):
	user = load_user(req.session)
	
	if user is None:
		import login as page
		render(req, page, goingto="usermach")
	
	elif "new" in req.fields:
		machineID = req.fields.getfirst("new", "")
		if not machineID.isdigit():
			raise "Machine ID is not a number"
		userMachine = UserMachine(userID=user.id, machineID=long(machineID))
		import user_machines as page
		render(req, page, userMachine=userMachine)
	
	elif "remove" in req.fields:
		userMachineID = long(req.fields.getfirst("remove", ""))
		userMachine = UserMachine.get(userMachineID)
		if userMachine.user != user:
			raise "This machine is not yours!"
		if len(userMachine.results) > 0:
			raise "This machine has results recorded for it"
		UserMachine.delete(userMachine.id)
		import user_machines as page
		render(req, page)
		
	elif "edit" in req.fields:
		userMachineID = req.fields.getfirst("edit", "")
		if not userMachineID.isdigit():
			raise "User machine ID is not a number"
		userMachine = UserMachine.get(userMachineID)
		if userMachine.user != user:
			raise "This machine is not yours!"
		import user_machine_edit as page
		render(req, page, user_machine=userMachine)
	
	elif "update" in req.fields:
		userMachineID = req.fields.getfirst("update", "")
		if not userMachineID.isdigit():
			raise "User machine ID is not a number"
		userMachine = UserMachine.get(userMachineID)
		val = req.fields.getfirst("settings", None)
		if val is not None: val = val.value
		userMachine.settings = val
		import user_machines as page
		render(req, page)
		
	else:
		import user_machines as page
		render(req, page)

# End usermach

@setup
def plot(req):
	user = load_user(req.session)
	
	if user is None:
		import login as page
		render(req, page)
	
	userMachineID = int(req.fields.getfirst("userMachineID"))
	userMachine = UserMachine.get(userMachineID)
	if userMachine.user != user:
		raise "This machine is not yours!"
	
	srs = SessionResult.select(
		SessionResult.q.userMachineID==userMachine.id,
		join=INNERJOINOn(
			Session, SessionResult,
			Session.q.id == SessionResult.q.sessionID,
		),
		orderBy=Session.q.started,
	)
	within = req.fields.getfirst("within", "")
	if within.isdigit():
		within = timedelta(int(within))
		lastSession = user.lastSession
		if lastSession is None:
			until = now()
		else:
			until = lastSession.started
		srs = srs.newClause(
			AND( srs.clause, Session.q.started >= (until - within) )
		)
	
	sessions, data = [], []
	ofwhat = req.fields.getfirst("of", "loading")
	
	for sr in srs:
		sessions.append(sr.session)
		if ofwhat == 'loading':
			data.append(sr.loading)
		elif ofwhat == 'duration':
			data.append(sr.duration)
	
	import matplotlib
	matplotlib.use('Agg')  # force the antigrain backend
	from matplotlib import rc
	from matplotlib.backends.backend_agg import FigureCanvasAgg
	from matplotlib.figure import Figure
	#from matplotlib.cbook import iterable
	from matplotlib.dates import date2num, MONDAY, \
		YearLocator, MonthLocator, WeekdayLocator, DayLocator, DateFormatter
	from matplotlib.ticker import MultipleLocator, ScalarFormatter, FuncFormatter
	
	# set some global properties that affect the defaults of all figures
	rc('lines', linewidth=4) # thicker plot lines
	##rc('grid', color=0.75, linestyle='-') # solid gray grid lines
	rc('grid', color='grey', linestyle='-') # solid gray grid lines
	rc('axes', hold=True, grid=True, facecolor='w')
	
	fig = Figure()
	ax = fig.add_axes([0.1, 0.15, 0.8, 0.76])
	
	starts = tuple( date2num(s.started) for s in sessions )
	
	c = ax.plot_date(starts, data, '-')
	for line in c:
		line.set_alpha(0.5)
	
	if ofwhat == 'loading':
		ax.set_title('Loadings / Time')
	elif ofwhat == 'duration':
		ax.set_title('Durations / Time')
	
	xr = max(starts) - min(starts)
	if xr <= 14:
		ax.xaxis.set_major_locator(DayLocator(2))
		ax.xaxis.set_major_formatter(DateFormatter('%d %b'))
	elif xr <= 42:
		ax.xaxis.set_major_locator(WeekdayLocator(MONDAY))
		ax.xaxis.set_major_formatter(DateFormatter('%d %b'))
	else:
		ax.xaxis.set_major_locator(MonthLocator())
		ax.xaxis.set_major_formatter(DateFormatter('%b'))
	
	yr = max(data) - min(data)
	if yr <= 10:
		ax.yaxis.set_major_locator(MultipleLocator(2))
	elif yr <= 50:
		ax.yaxis.set_major_locator(MultipleLocator(5))
	else:
		ax.yaxis.set_major_locator(MultipleLocator(10))
	ax.yaxis.set_major_formatter(ScalarFormatter())
	#ax.autoscale_view()
	ax.zoomy(-1)
	
	for label in ax.get_xticklabels():
		label.set_rotation(45)
		label.set_fontsize(13)
	
	for label in ax.get_yticklabels():
		label.set_fontsize(13)
	
	canvas = FigureCanvasAgg(fig)
	
	from tempfile import mkdtemp
	from os.path import join
	d = mkdtemp()
	f = join(d, "image.png")
	try:
		canvas.print_figure(f, dpi=55)
		req.content_type = "image/png"
		req.sendfile(f)
	finally:
		os.unlink(f)
		os.rmdir(d)
	
# End plot


handlers = dict(
	login=login,
	logout=logout,
	home=home,
	sessions=sessions,
	usermach=usermach,
	plot=plot,
)
handlers[''] = index

def handler(req):
	uri, command = req.uri.rsplit("/", 1)
	req.log_error("uri: %r, command: %r" % (uri, command), apache.APLOG_NOTICE)
	
	if command in handlers:
		handler = handlers[command]
	else:
		return DECLINED
	
	started = now()
	
	req.base_uri = uri
	req.fields = util.FieldStorage(req)
	req.session = WebSession(req)
	
	try:
		try:
			return handler(req)
		except:
			typ, val, tb = sys.exc_info()
			if isinstance(typ, basestring):
				import error as page
				render(req, page, error=typ)
				return OK
			else:
				raise
	finally:
		req.session.save()
		req.log_error(
			"command %r took %s" % (command, now() - started),
			apache.APLOG_NOTICE
		)

# End handle

# End
