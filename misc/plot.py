from kieser.stat.runtime import *
from sqlobject.sqlbuilder import JOIN, INNERJOINOn

user = User.get(1)

userMachine = user.userMachines[0]

srs = SessionResult.select(
	SessionResult.q.userMachineID==userMachine.id,
	join=INNERJOINOn(
		Session, SessionResult,
		Session.q.id == SessionResult.q.sessionID,
	),
	orderBy=Session.q.started,
)
within = "30"
if within.isdigit():
	within = timedelta(int(within))
	lastSession = user.lastSession
	if lastSession is None:
		until = now()
	else:
		until = lastSession.started
	srs = srs.newClause(
		AND(srs.clause, Session.q.started >= (until - within))
	)
	print "until-within=%r" % (until-within)

sessions, data = [], []

ofwhat = "loading"

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
rc('lines', linewidth=2) # thicker plot lines
rc('grid', color=0.75, linestyle='-') # solid gray grid lines
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
ax.autoscale_view()

for label in ax.get_xticklabels():
	label.set_rotation(45)
	label.set_fontsize(13)

for label in ax.get_yticklabels():
	label.set_fontsize(13)

def save(fig, filename):
	canvas = FigureCanvasAgg(fig)
	canvas.print_figure(filename, dpi=55)

