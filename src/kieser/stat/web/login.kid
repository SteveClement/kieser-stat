<?python goingto = None ?>

<html xmlns:py="http://purl.org/kid/ns#" py:extends="'base.kid'">

<head>
	<title>Login</title>
	<style type="text/css">
		#content td { text-align: right; }
	</style>
</head>

<body>
<content>
	<form action="${this}/login" method="POST" accept-charset="UTF-8">
	<input type="hidden" py:if="goingto is not None" name="goingto" value="$goingto" />
	<table>
	<tr>
		<td><label for="userID">User name:</label></td>
		<td><input type="text" name="userID" value="steve" id="userID" size="20" tabindex="1" /></td>
		<td rowspan="2"><input type="submit" name="login" value="Log-in"
			style="display:block; height:100%" /></td>
	</tr>
	<tr>
		<td><label for="password">Password:</label></td>
		<td><input type="password" name="password" value="foobar" id="password" size="20" tabindex="1" /></td>
	</tr>
	</table>
	</form>
</content>
</body>

</html>
