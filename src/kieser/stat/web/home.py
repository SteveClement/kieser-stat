# -*- coding: utf-8 -*-
# Kid template module
kid_version = '0.9.6'
kid_file = 'src/kieser/stat/web/home.kid'
import kid
from kid.template_util import *
import kid.template_util as template_util
_def_names = []
encoding = "utf-8"
doctype = None
omit_namespaces = [kid.KID_XMLNS]
layout_params = {}
def pull(**kw): return Template(**kw).pull()
def generate(encoding=encoding, fragment=False, output=None, format=None, **kw): return Template(**kw).generate(encoding=encoding, fragment=fragment, output=output, format=format)
def serialize(encoding=encoding, fragment=False, output=None, format=None, **kw): return Template(**kw).serialize(encoding=encoding, fragment=fragment, output=output, format=format)
def write(file, encoding=encoding, fragment=False, output=None, format=None, **kw): return Template(**kw).write(file, encoding=encoding, fragment=fragment, output=output, format=format)
def initialize(template): pass
BaseTemplate = kid.BaseTemplate
BaseTemplate1 = template_util.base_class_extends("'base.kid'", globals(), {}, "'base.kid'")
class Template(BaseTemplate1, BaseTemplate):
	_match_templates = []
	def initialize(self):
		rslt = initialize(self)
		if rslt != 0: super(Template, self).initialize()
	def _pull(self):
		exec template_util.get_locals(self, locals())
		current, ancestors = None, []
		if doctype: yield DOCTYPE, doctype
		ancestors.insert(0, current)
		current = Element(u'html', {})
		for _p, _u in {u'py': u'http://purl.org/kid/ns#'}.items():
			if not _u in omit_namespaces: yield START_NS, (_p,_u)
		yield START, current
		yield TEXT, u'\n\n'
		ancestors.insert(0, current)
		current = Element(u'head', {})
		yield START, current
		yield TEXT, u'\n\t'
		ancestors.insert(0, current)
		current = Element(u'title', {})
		yield START, current
		yield TEXT, u'Home'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t'
		ancestors.insert(0, current)
		current = Element(u'style', {u'type': u'text/css'})
		yield START, current
		yield TEXT, u'\n\tth {\n\t\twhite-space: nowrap;\n\t}\n\tth.selected {\n\t\tbackground-color: limegreen;\n\t}\n\tth.highlight {\n\t\tbackground-color: limegreen;\n\t}\n\tth a {\n\t\ttext-decoration: none;\n\t\tcolor: white;\n\t}\n\tth a:hover {\n\t\tcolor: limegreen;\n\t}\n\tth.selected a:hover {\n\t\tcolor: white;\n\t}\n\t'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t'
		ancestors.insert(0, current)
		current = Element(u'script', {u'type': u'text/javascript'})
		yield START, current
		yield TEXT, u'\n\t\n\tvar selected = {};\n\tvar graphs = {};\n\t\n\tfunction toggleplot(link, of, umid, within) {\n\t\tvar img = getElement("plot-" + umid);\n\t\tvar imgrow = img.parentNode.parentNode; \n\t\tvar link = getElement(link);\n\t\tvar linkcell = link.parentNode;\n\t\t\n\t\tif (hasElementClass(linkcell, \'selected\')) {\n\t\t\tselected[umid] = undefined;\n\t\t\tremoveElementClass(linkcell, "selected");\n\t\t\taddElementClass(imgrow, "invisible");\n\t\t}\n\t\telse {\n\t\t\tvar src = \'plot?userMachineID=\' + umid + \';of=\' + of;\n\t\t\tif (within) {\n\t\t\t\tsrc += \';within=\' + within;\n\t\t\t}\n\t\t\t\n\t\t\tvar graph = graphs[src];\n\t\t\t\n\t\t\tif (graph) {\n\t\t\t\tif (graph.complete) {\n\t\t\t\t\timg.src = graph.src;\n\t\t\t\t}\n\t\t\t\telse {\n\t\t\t\t\timg.src = loading.src;\n\t\t\t\t}\n\t\t\t}\n\t\t\telse {\n\t\t\t\timg.src = loading.src;\n\t\t\t\tgraph = new Image();\n\t\t\t\tgraphs[src] = graph;\n\t\t\t\tgraph.onload = function() { img.src = graph.src; };\n\t\t\t\tgraph.onabort = function() { graphs[src] = undefined; };\n\t\t\t\tgraph.onerror = function() { alert("Error while loading graph"); };\n\t\t\t\tgraph.src = src;\n\t\t\t}\n\t\t\t\n\t\t\tif (selected[umid])\n\t\t\t\tremoveElementClass(selected[umid].parentNode, "selected");\n\t\t\tselected[umid] = link;\n\t\t\t\n\t\t\taddElementClass(linkcell, "selected");\n\t\t\tremoveElementClass(imgrow, "invisible");\n\t\t}\n\t}\n\t\n\tvar demoLinks = null;\n\tvar demoLink = null;\n\tvar demoRunning = false;\n\t\n\tfunction setupDemo() {\n\t\tif (!isNull(demoLinks)) {\n\t\t\treturn true;\n\t\t}\n\t\t\n\t\tvar links = getElementsByTagAndClassName(\'a\', \'graphlink\');\n\t\tif (links.length == 0) {\n\t\t\treturn false;\n\t\t}\n\t\t\n\t\tdemoLinks = map(\n\t\t\tfunction(link) {\n\t\t\t\tvar onclick = link.onclick;\n\t\t\t\tlink.onclick = function () {\n\t\t\t\t\tif (!isNull(demoLink)) {\n\t\t\t\t\t\tif (this != demoLink.link) {\n\t\t\t\t\t\t\tdemoLink.toggle();\n\t\t\t\t\t\t}\n\t\t\t\t\t\tdemoLink = null;\n\t\t\t\t\t}\n\t\t\t\t\tdemoRunning = false;\n\t\t\t\t\tlink.onclick = onclick;\n\t\t\t\t\treturn link.onclick();\n\t\t\t\t};\n\t\t\t\treturn {\n\t\t\t\t\t\'link\':link, \'toggle\':bind(onclick, link)\n\t\t\t\t};\n\t\t\t},\n\t\t\tlinks\n\t\t);\n\t\t\n\t\treturn true;\n\t}\n\t\n\tfunction demoTransition(next, num) {\n\t\tvar th = next.link.parentNode;\n\t\t\n\t\tif (num % 2) {\n\t\t\taddElementClass(th, "highlight");\n\t\t\tcallLater(0.200, demoTransition, next, num+1);\n\t\t}\n\t\telse {\n\t\t\tremoveElementClass(th, "highlight");\n\t\t\t\n\t\t\tif (demoRunning) {\n\t\t\t\tif (num == 10) {\n\t\t\t\t\tif (demoLink) demoLink.toggle();\n\t\t\t\t\tdemoLink = next;\n\t\t\t\t\tdemoLink.toggle();\n\t\t\t\t\tcallLater(6.5, demoNext);\n\t\t\t\t}\n\t\t\t\telse {\n\t\t\t\t\tcallLater(0.200, demoTransition, next, num+1);\n\t\t\t\t}\n\t\t\t}\n\t\t}\n\t}\n\t\n\tfunction demoNext() {\n\t\tvar len = demoLinks.length;\n\t\tvar jump = Math.floor( Math.random() * (len-1) );\n\t\t\n\t\tif (!isNull(demoLink)) {\n\t\t\tjump += demoLink.index;\n\t\t}\n\t\t\n\t\tvar index = jump % len;\n\t\tvar next = demoLinks[index];\n\t\tnext.index = index;\n\t\t\n\t\tif (demoRunning) {\n\t\t\tdemoTransition(next, 1); \n\t\t}\n\t}\n\t\n\tfunction startDemo() {\n\t\t//createLoggingPane(true);\n\t\t\n\t\tif (demoRunning) {\n\t\t\treturn true;\n\t\t}\n\t\telse if (setupDemo()) {\n\t\t\tdemoRunning = true;\n\t\t\tcallLater(1, demoNext);\n\t\t\treturn true;\n\t\t}\n\t\telse {\n\t\t\treturn false;\n\t\t}\n\t}\n\t\n\taddLoadEvent(startDemo);\n\t\n\t'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\n'
		ancestors.insert(0, current)
		current = Element(u'body', {})
		yield START, current
		yield TEXT, u'\n'
		ancestors.insert(0, current)
		current = Element(u'menubar', {})
		yield START, current
		yield TEXT, u'\n'
		ancestors.insert(0, current)
		current = Element(u'a', template_util.make_attrib({u'href': [this, u'/sessions']}, self._get_assume_encoding()))
		yield START, current
		yield TEXT, u'Sessions'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n'
		ancestors.insert(0, current)
		current = Element(u'a', template_util.make_attrib({u'href': [this, u'/usermach']}, self._get_assume_encoding()))
		yield START, current
		yield TEXT, u'Your machines'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n'
		_e = Comment(u'a href="javascript:alert(\'Administration is not implemented yet\')">Administration</a')
		yield START, _e; yield END, _e; del _e
		yield TEXT, u'\n'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n'
		ancestors.insert(0, current)
		current = Element(u'content', {})
		yield START, current
		yield TEXT, u'\n\t'
		ancestors.insert(0, current)
		current = Element(u'h2', {})
		yield START, current
		for _e in [u'Welcome ', user.firstName]:
			for _e2 in template_util.generate_content(_e): yield _e2
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t\n\t'
		ancestors.insert(0, current)
		current = Element(u'table', {u'style': u'height:100%'})
		yield START, current
		yield TEXT, u'\n\t'
		for um in user.userMachines:
			yield TEXT, u'\n\t\t'
			m = um.machine
			yield TEXT, u'\n\t\t'
			ancestors.insert(0, current)
			current = Element(u'tr', {})
			yield START, current
			yield TEXT, u'\n\t\t\t'
			ancestors.insert(0, current)
			current = Element(u'th', {})
			yield START, current
			for _e in [m.name, u' - ', m.description]:
				for _e2 in template_util.generate_content(_e): yield _e2
			yield END, current
			current = ancestors.pop(0)
			yield TEXT, u'\n\t\t\t'
			ancestors.insert(0, current)
			current = Element(u'th', {})
			yield START, current
			ancestors.insert(0, current)
			current = Element(u'a', template_util.make_attrib({u'href': u'#', u'class': u'graphlink', u'onclick': [u"toggleplot(this,'loading',", um.id, u',31)']}, self._get_assume_encoding()))
			yield START, current
			yield TEXT, u'Recent loadings'
			yield END, current
			current = ancestors.pop(0)
			yield END, current
			current = ancestors.pop(0)
			yield TEXT, u' \n\t\t\t'
			ancestors.insert(0, current)
			current = Element(u'th', {})
			yield START, current
			ancestors.insert(0, current)
			current = Element(u'a', template_util.make_attrib({u'href': u'#', u'class': u'graphlink', u'onclick': [u"toggleplot(this,'loading',", um.id, u')']}, self._get_assume_encoding()))
			yield START, current
			yield TEXT, u'All loadings'
			yield END, current
			current = ancestors.pop(0)
			yield END, current
			current = ancestors.pop(0)
			yield TEXT, u'\n\t\t\t'
			ancestors.insert(0, current)
			current = Element(u'th', {})
			yield START, current
			ancestors.insert(0, current)
			current = Element(u'a', template_util.make_attrib({u'href': u'#', u'class': u'graphlink', u'onclick': [u"toggleplot(this,'duration',", um.id, u',31)']}, self._get_assume_encoding()))
			yield START, current
			yield TEXT, u'Recent durations'
			yield END, current
			current = ancestors.pop(0)
			yield END, current
			current = ancestors.pop(0)
			yield TEXT, u' \n\t\t\t'
			ancestors.insert(0, current)
			current = Element(u'th', {})
			yield START, current
			ancestors.insert(0, current)
			current = Element(u'a', template_util.make_attrib({u'href': u'#', u'class': u'graphlink', u'onclick': [u"toggleplot(this,'duration',", um.id, u')']}, self._get_assume_encoding()))
			yield START, current
			yield TEXT, u'All durations'
			yield END, current
			current = ancestors.pop(0)
			yield END, current
			current = ancestors.pop(0)
			yield TEXT, u'\n\t\t'
			yield END, current
			current = ancestors.pop(0)
			yield TEXT, u'\n\t\t'
			ancestors.insert(0, current)
			current = Element(u'tr', {u'class': u'invisible'})
			yield START, current
			yield TEXT, u'\n\t\t\t'
			ancestors.insert(0, current)
			current = Element(u'td', {u'colspan': u'5', u'style': u'text-align:center'})
			yield START, current
			yield TEXT, u'\n\t\t\t\t'
			ancestors.insert(0, current)
			current = Element(u'img', template_util.make_attrib({u'src': u'loading.gif', u'alt': u'Loading', u'id': [u'plot-', um.id]}, self._get_assume_encoding()))
			yield START, current
			yield END, current
			current = ancestors.pop(0)
			yield TEXT, u'\n\t\t\t'
			yield END, current
			current = ancestors.pop(0)
			yield TEXT, u'\n\t\t'
			yield END, current
			current = ancestors.pop(0)
			yield TEXT, u'\n\t'
		yield TEXT, u'\n\t'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t\n'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\n'
		yield END, current
		current = ancestors.pop(0)
