<?python
from kieser.stat.runtime import *
rowclass = "even", "odd"
?>

<html xmlns:py="http://purl.org/kid/ns#" py:extends="'base.kid'">

<head>
	<title>Your Machines</title>
</head>

<body>
<menubar>
<a href="${this}/home">Home</a>
<a href="${this}/sessions">Sessions</a>
</menubar>
<content>
	<h2>Your machines</h2>
	<table id="user-machines">
	<tr class="greybg">
		<th style="width: 16em;">Name</th>
		<th style="width: 20em;">Settings</th>
		<th>Actions</th>
	</tr>
	<tr py:for="row, user_machine in enumerate(user.userMachines)" class="${rowclass[row%2]}">
		<?python machine = user_machine.machine ?>
		<td>${machine.name} - ${machine.description}</td>
		<td style="white-space:pre" py:content="user_machine.settings or '-'" />
		<td>
			<form action="${req.uri}" method="GET" accept-charset="UTF-8">
			<input type="hidden" name="edit" value="${user_machine.id}" />
			<input type="submit" value="Edit" />
			</form>
			<form action="${req.uri}" method="POST" accept-charset="UTF-8">
			<input type="hidden" name="remove" value="${user_machine.id}" />
			<input type="submit" value="Remove" />
			</form>
		</td>
	</tr>
	</table>
	
	<?python
	already = set([ um.machine for um in user.userMachines ])
	machines = [ m for m in Machine.select(orderBy="name") if m not in already ]
	?>
	<form action="${req.uri}" method="POST" py:if="len(machines)" accept-charset="UTF-8">
	<select name="new">
	<option py:for="machine in machines"
		value="${machine.id}">${machine.name} - ${machine.description}</option>
	</select>
	<input type="submit" value="Add machine" />
	</form>
	
</content>
</body>

</html>
