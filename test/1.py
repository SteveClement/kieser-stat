from ion.gym.runtime import *

user = User.byUserIDOrCreate("gavin")

if not user.surname:
	user.surname = "Panella"
if not user.firstName:
	user.firstName = "Gavin"

machines = tuple(Machines.select())
if not machines:
	Machine(name="A1"

	
	
	
userMachines = user.userMachines
if not userMachines:
	UserMachine(user=user, 
	




# End
