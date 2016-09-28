<?python title, error = "Error", None ?>
<html xmlns:py="http://purl.org/kid/ns#" py:extends="'base.kid'">
<head>
	<title py:content="title">Error</title>
	<style type="text/css">
		#content {
			border-left: 5px solid red;
			padding-left: 1em;
		}
		#message {
			font-size: larger;
		}
	</style>
</head>

<body>
<content>
	<p py:if="error" py:content="error" id="message">Error message</p>
</content>
</body>

</html>
