<html xmlns:py="http://purl.org/kid/ns#" py:extends="'base.kid'">

<head>
	<title>Home</title>
	<style type="text/css">
	th {
		white-space: nowrap;
	}
	th.selected {
		background-color: limegreen;
	}
	th.highlight {
		background-color: limegreen;
	}
	th a {
		text-decoration: none;
		color: white;
	}
	th a:hover {
		color: limegreen;
	}
	th.selected a:hover {
		color: white;
	}
	</style>
	<script type="text/javascript">
	
	var selected = {};
	var graphs = {};
	
	function toggleplot(link, of, umid, within) {
		var img = getElement("plot-" + umid);
		var imgrow = img.parentNode.parentNode; 
		var link = getElement(link);
		var linkcell = link.parentNode;
		
		if (hasElementClass(linkcell, 'selected')) {
			selected[umid] = undefined;
			removeElementClass(linkcell, "selected");
			addElementClass(imgrow, "invisible");
		}
		else {
			var src = 'plot?userMachineID=' + umid + ';of=' + of;
			if (within) {
				src += ';within=' + within;
			}
			
			var graph = graphs[src];
			
			if (graph) {
				if (graph.complete) {
					img.src = graph.src;
				}
				else {
					img.src = loading.src;
				}
			}
			else {
				img.src = loading.src;
				graph = new Image();
				graphs[src] = graph;
				graph.onload = function() { img.src = graph.src; };
				graph.onabort = function() { graphs[src] = undefined; };
				graph.onerror = function() { alert("Error while loading graph"); };
				graph.src = src;
			}
			
			if (selected[umid])
				removeElementClass(selected[umid].parentNode, "selected");
			selected[umid] = link;
			
			addElementClass(linkcell, "selected");
			removeElementClass(imgrow, "invisible");
		}
	}
	
	var demoLinks = null;
	var demoLink = null;
	var demoRunning = false;
	
	function setupDemo() {
		if (!isNull(demoLinks)) {
			return true;
		}
		
		var links = getElementsByTagAndClassName('a', 'graphlink');
		if (links.length == 0) {
			return false;
		}
		
		demoLinks = map(
			function(link) {
				var onclick = link.onclick;
				link.onclick = function () {
					if (!isNull(demoLink)) {
						if (this != demoLink.link) {
							demoLink.toggle();
						}
						demoLink = null;
					}
					demoRunning = false;
					link.onclick = onclick;
					return link.onclick();
				};
				return {
					'link':link, 'toggle':bind(onclick, link)
				};
			},
			links
		);
		
		return true;
	}
	
	function demoTransition(next, num) {
		var th = next.link.parentNode;
		
		if (num % 2) {
			addElementClass(th, "highlight");
			callLater(0.200, demoTransition, next, num+1);
		}
		else {
			removeElementClass(th, "highlight");
			
			if (demoRunning) {
				if (num == 10) {
					if (demoLink) demoLink.toggle();
					demoLink = next;
					demoLink.toggle();
					callLater(6.5, demoNext);
				}
				else {
					callLater(0.200, demoTransition, next, num+1);
				}
			}
		}
	}
	
	function demoNext() {
		var len = demoLinks.length;
		var jump = Math.floor( Math.random() * (len-1) );
		
		if (!isNull(demoLink)) {
			jump += demoLink.index;
		}
		
		var index = jump % len;
		var next = demoLinks[index];
		next.index = index;
		
		if (demoRunning) {
			demoTransition(next, 1); 
		}
	}
	
	function startDemo() {
		//createLoggingPane(true);
		
		if (demoRunning) {
			return true;
		}
		else if (setupDemo()) {
			demoRunning = true;
			callLater(1, demoNext);
			return true;
		}
		else {
			return false;
		}
	}
	
	addLoadEvent(startDemo);
	
	</script>
</head>

<body>
<menubar>
<a href="${this}/sessions">Sessions</a>
<a href="${this}/usermach">Your machines</a>
<!--a href="javascript:alert('Administration is not implemented yet')">Administration</a-->
</menubar>
<content>
	<h2>Welcome ${user.firstName}</h2>
	
	<table style="height:100%">
	<div py:strip="" py:for="um in user.userMachines">
		<?python m = um.machine ?>
		<tr>
			<th>${m.name} - ${m.description}</th>
			<th><a href="#" class="graphlink"
				onclick="toggleplot(this,'loading',${um.id},31)">Recent loadings</a></th> 
			<th><a href="#" class="graphlink"
				onclick="toggleplot(this,'loading',${um.id})">All loadings</a></th>
			<th><a href="#" class="graphlink"
				onclick="toggleplot(this,'duration',${um.id},31)">Recent durations</a></th> 
			<th><a href="#" class="graphlink"
				onclick="toggleplot(this,'duration',${um.id})">All durations</a></th>
		</tr>
		<tr class="invisible">
			<td colspan="5"  style="text-align:center">
				<img src="loading.gif" id="plot-${um.id}" alt="Loading" />
			</td>
		</tr>
	</div>
	</table>
	
</content>
</body>

</html>
