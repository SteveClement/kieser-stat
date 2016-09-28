<?python from kieser.stat.runtime import * ?>

<html xmlns:py="http://purl.org/kid/ns#" py:extends="'base.kid'">

<head>
	<title>User Machines</title>
</head>

<body>
<menubar>
<a href="${this}/home">Home</a>
<a href="${this}/sessions">Sessions</a>
<a href="${this}/usermach">Your machines</a>
</menubar>
<content>
	<?python machine = user_machine.machine ?>
	
	<h2>Editing machine ${machine.name} - ${machine.description}</h2>
	
	<form action="${req.uri}" method="POST" accept-charset="UTF-8">
	<input type="hidden" name="update" value="${user_machine.id}" />
	<table id="user-machines">
	<tr class="greybg">
		<th style="width: 24em;">Settings</th>
	</tr>
	<tr>
		<td>
<textarea rows="7" cols="55" name="settings" id="settings">${user_machine.settings}</textarea>
<script type="text/javascript">focusOnLoad('settings');</script>
		</td>
	</tr>
	</table>
	<input type="submit" value="Save changes" />
	</form>
	
</content>
</body>

</html>
