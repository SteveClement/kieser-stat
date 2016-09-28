<html xmlns:py="http://purl.org/kid/ns#" py:extends="'base.kid'">

<head>
	<title>Sessions</title>
</head>

<body>
<menubar>
<a href="${this}/home">Home</a>
<a href="${this}/usermach">Your machines</a>
</menubar>
<content>
	<h2>Sessions</h2>
	
	<form action="${req.uri}" method="POST" accept-charset="UTF-8">
	<div><input type="submit" name="new" value="New session" /></div>
	</form>
	
	<table style="margin-top: 0.5em">
	<tr class="greybg">
		<th>Date</th>
		<th>Day</th>
		<th>Time</th>
		<th>Duration</th>
		<th>Notes</th>
		<th>Actions</th>
	</tr>
	<?python
		sessions = user.sessions
		def key(session): return session.started
		sessions.sort(key=key, reverse=True)
		rowclass = "even", "odd"
	?>
	<tr py:for="row, session in enumerate(sessions)" class="${rowclass[row%2]}">
		<td style="text-align: center" py:content="session.started.strftime('%d %B %Y')" />
		<td style="text-align: center" py:content="session.started.strftime('%A')" />
		<td style="text-align: center" py:content="session.started.strftime('%H:%M')" />
		<?python
			duration = session.duration
			if duration:
				hours, seconds = divmod(duration.seconds, 3600)
				minutes = seconds/60
				if hours and minutes:
					duration = "%d hour%s %d mins" % (
						hours, (not hours == 1) and 's' or '', minutes,
					)
				elif hours:
					duration = "%d hour%s" % (
						hours, (not hours == 1) and 's' or '',
					)
				else:
					duration = "%d mins" % minutes
		?>
		<td style="text-align: center" py:content="duration or '-'" />
		<td style="white-space:pre" py:content="session.notes or '-'"></td>
		<td style="text-align: center">
			<form action="${req.uri}" method="GET" accept-charset="UTF-8">
			<div>
			<input type="hidden" name="edit" value="${session.id}" />
			<input type="submit" value="Edit" />
			</div>
			</form>
		</td>
	</tr>
	</table>
	
</content>
</body>

</html>
