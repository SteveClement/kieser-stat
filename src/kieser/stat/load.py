from datetime import datetime
from kieser.stat.runtime import *
from sys import argv, stdin

def load_data(fin=stdin):
	for line in fin:
		if line.isspace():
			continue
		
		if line.startswith('~'):
			elems = line[1:].split()
			args = dict(
				zip(
					("userID", "firstName", "surname"),
					elems,
				)
			)
			user = User.byUserIDOrCreate(args.pop('userID'))
			user.set(**args)
			continue
		
		line = line.split()
		date = line.pop(0)
		
		if date.isdigit():
			year = int(date)
			machines = []
			for name in line:
				try:
					machine = Machine.byName(name)
				except SQLObjectNotFound:
					machine = Machine(name=name,
						description="%s's machine" % user.firstName)
				machines.append(machine)
		
		else:
			day, month = map(int, date.split("/"))
			date = datetime(year, month, day)
			session = Session(user=user, started=date)
			for machine, res in zip(machines, line):
				if res == '-':
					continue
				else:
					loading, duration = map(int, res.split("/"))
				
				um = tuple(UserMachine.select(
					AND(
						UserMachine.q.userID==user.id,
						UserMachine.q.machineID==machine.id,
					),
				))
				if um:
					um = um[0]
				else:
					um = UserMachine(userID=user.id, machineID=machine.id)
				
				sr = SessionResult(
					session=session, userMachine=um,
					loading=loading, duration=duration,
				)

if __name__ == '__main__':
	for datafile in argv[1:]:
		if datafile == '-':
			load_data()
		else:
			din = open(datafile, "rb")
			load_data(din)
			din.close()


