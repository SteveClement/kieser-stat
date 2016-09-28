<?python
from kieser.stat.runtime import *
rowclass = "even", "odd"
?>

<html xmlns:py="http://purl.org/kid/ns#" py:extends="'base.kid'">

<head>
	<title>Sessions</title>
	<script type="text/javascript">
	function incr(name, delta) {
		elem = getElement(name);
		val = parseInt(elem.value);
		if (isNaN(elem.value))
			return true;
		diff = val % delta;
		if (diff == 0)
			val += delta;
		else
			if (0 > delta)
				val -= diff;
			else if (delta > 0)
				val += delta - diff;
		elem.value = val;
		return true;
	}
	</script>
</head>

<body>
<menubar>
<a href="${this}/home">Home</a>
<a href="${this}/sessions">Sessions</a>
<a href="${this}/usermach">Your machines</a>
</menubar>
<content>
	<h2>Edit session for ${user.surname}, ${user.firstName}</h2>
	<form action="${req.uri}" method="POST" accept-charset="UTF-8">
	<input type="hidden" name="update" value="${session.id}" />
	
	<table>
	<tr class="greybg">
		<th style="width: 12em;">Date</th>
		<th style="width: 12em;">Time</th>
		<th style="width: 12em;">Duration</th>
	</tr>
	<tr>
		<td style="text-align: center" py:content="date_field('started', session.started)" />
		<td style="text-align: center" py:content="time_field('started', session.started)" />
		<td style="text-align: center" py:content="duration_field('duration', session.duration)" />
	</tr>
	<tr class="greybg">
		<th colspan="3" style="width: 12em;">Notes</th>
	</tr>
	<tr>
		<td colspan="3" style="text-align: center">
<textarea cols="70" rows="4" name="notes">${session.notes}</textarea>
		</td>
	</tr>
	</table>
	
	<table>
	<tr class="greybg">
		<th style="width: 16em;">Name</th>
		<th style="width: 20em;">Settings</th>
		<th>Loading</th>
		<th>Duration</th>
	</tr>
	<?python results = dict([ (r.userMachine, r) for r in session.results ]) ?>
	<tr py:for="row, um in enumerate(user.userMachines)" class="${rowclass[row%2]}">
		<?python
			m, res = um.machine, results.get(um, None)
			if res:
				loading, duration = res.loading, res.duration
			else:
				loading, duration = None, None
		?>
		<input type="hidden" name="userMachineID" value="${um.id}" />
		<td>${m.name} - ${m.description}</td>
		<td style="white-space:pre" py:content="um.settings or '-'" />
		<td>
		<input type="button" style="width: 1.6em" value="-" onclick="incr('loading-${um.id}',-2)" />
		<input type="text" size="7" name="loading-${um.id}" style="text-align: center"
			id="loading-${um.id}" value="${loading}" />
		<input type="button" style="width: 1.6em" value="+" onclick="incr('loading-${um.id}',+2)" />
		</td>
		<td>
		<input type="button" style="width: 1.6em" value="-" onclick="incr('duration-${um.id}',-5)" />
		<input type="text" size="7" name="duration-${um.id}" style="text-align: center"
			id="duration-${um.id}" value="${duration}" />
		<input type="button" style="width: 1.6em" value="+" onclick="incr('duration-${um.id}',+5)" />
		</td>
	</tr>
	</table>
	
	<input type="submit" value="Save changes" />
	</form>
</content>
</body>

</html>
