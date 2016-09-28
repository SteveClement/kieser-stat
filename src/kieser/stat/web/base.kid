<?python from datetime import date, time, datetime ?>

<?python
months = \
	"January February March April May June July " \
	"August September October November December"
months = dict( (i+1,m) for (i,m) in enumerate(months.split()) )
message = None
?>

<html xmlns:py="http://purl.org/kid/ns#">

<head py:match="item.tag == '{http://www.w3.org/1999/xhtml}head'">
	<?python
		titles = filter(lambda item: item.tag == 'title', item)
		if titles:
			title = titles[0]
			item.remove(title)
			title = title.text
	?>
	<title>
		Kieser Training Customer Portal
		<span py:strip="" py:if="title"> - ${title}</span>
	</title>
	<link rel="shortcut icon" href="kieser-icon.png" />
	<link rel="stylesheet" href="base.css" title="Base styles" type="text/css" />
	<script type="text/javascript" src="js/MochiKit/MochiKit.js" />
	<script type="text/javascript">
	var loading = new Image();
	loading.src = "loading.gif";
	</script>
	<div py:for="node in item" py:replace="node" />
</head>

<body py:match="item.tag == '{http://www.w3.org/1999/xhtml}body'">
	<div id="usernote" py:if="user is not None">${user.surname}, ${user.firstName}</div>
	
	<h1 id="header">
		<img src="kieser-logo.gif" alt="Kieser Training logo" />
		Kieser Training Customer Portal
	</h1>
	
	<div id="menubar">
		<div py:for="node in item.findall('menubar/a')" py:replace="node" />
		<a py:if="user is not None" href="${this}/logout">Logout <strong>${user.userID}</strong></a>
	</div>
	
	<div id="content">
		<p py:if="message" style="color:red">$message</p>
		<div py:for="node in item.findall('content/*')" py:replace="node" />
	</div>
	
</body>

<div py:def="date_field(name, dt)" py:strip="">
	<span style="white-space: nowrap">
		<select name="${name}-day">
		<option py:for="day in range(1,32)"
			py:attrs="(day == dt.day) and {'selected':'selected'} or {}">${'%02d' % day}</option>
		</select>
		<select name="${name}-month">
		<option py:for="month in range(1,13)"
			py:attrs="(month == dt.month) and {'selected':'selected'} or {}"
			value="$month">${months[month]}</option>
		</select>
		<select name="${name}-year">
		<option py:for="year in range(2000,datetime.now().year+1)"
			py:attrs="(year == dt.year) and {'selected':'selected'} or {}">${year}</option>
		</select>
	</span>
</div>

<div py:def="time_field(name, dt)" py:strip="">
	<span style="white-space: nowrap">
		<select name="${name}-hour">
		<option py:for="hour in range(0,24)"
			py:attrs="(hour == dt.hour) and {'selected':'selected'} or {}">${'%02d' % hour}</option>
		</select>
		<select name="${name}-minute">
		<option py:for="minute in range(0,60,5)"
			py:attrs="(minute &lt;= dt.minute &lt; minute+5) and {'selected':'selected'} or {}">${'%02d' % minute}</option>
		</select>
	</span>
</div>

<div py:def="duration_field(name, dt)" py:strip="">
	<span style="white-space: nowrap">
		<?python
			if isinstance(dt, basestring):
				hours, minutes = map(int, dt.split(":"))
			else:
				hours, seconds = divmod(dt.seconds, 3600)
				hours += (dt.days * 24)
				minutes = seconds // 60
		?>
		<select name="${name}-hours">
		<option py:for="hour in range(0,5)"
			py:attrs="(hour == hours) and {'selected':'selected'} or {}">$hour</option>
		</select> hours
		<select name="${name}-minutes">
		<option py:for="minute in range(0,60,5)"
			py:attrs="(minute &lt;= minutes &lt; minute+5) and {'selected':'selected'} or {}">${'%02d' % minute}</option>
		</select> minutes
	</span>
</div>

<div py:def="datetime_field(name, dt)" py:strip="">
	<div py:replace="date_field(name, dt)" />
	<div py:replace="time_field(name, dt)" />
</div>

</html>
