# -*- coding: utf-8 -*-
# Kid template module
kid_version = '0.9.6'
kid_file = 'src/kieser/stat/web/session_edit.kid'
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
from kieser.stat.runtime import *
rowclass = "even", "odd"
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
		yield TEXT, u'Sessions'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t'
		ancestors.insert(0, current)
		current = Element(u'script', {u'type': u'text/javascript'})
		yield START, current
		yield TEXT, u'\n\tfunction incr(name, delta) {\n\t\telem = getElement(name);\n\t\tval = parseInt(elem.value);\n\t\tif (isNaN(elem.value))\n\t\t\treturn true;\n\t\tdiff = val % delta;\n\t\tif (diff == 0)\n\t\t\tval += delta;\n\t\telse\n\t\t\tif (0 > delta)\n\t\t\t\tval -= diff;\n\t\t\telse if (delta > 0)\n\t\t\t\tval += delta - diff;\n\t\telem.value = val;\n\t\treturn true;\n\t}\n\t'
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
		current = Element(u'a', template_util.make_attrib({u'href': [this, u'/home']}, self._get_assume_encoding()))
		yield START, current
		yield TEXT, u'Home'
		yield END, current
		current = ancestors.pop(0)
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
		for _e in [u'Edit session for ', user.surname, u', ', user.firstName]:
			for _e2 in template_util.generate_content(_e): yield _e2
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t'
		ancestors.insert(0, current)
		current = Element(u'form', template_util.make_attrib({u'action': [req.uri], u'accept-charset': u'UTF-8', u'method': u'POST'}, self._get_assume_encoding()))
		yield START, current
		yield TEXT, u'\n\t'
		ancestors.insert(0, current)
		current = Element(u'input', template_util.make_attrib({u'type': u'hidden', u'name': u'update', u'value': [session.id]}, self._get_assume_encoding()))
		yield START, current
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t\n\t'
		ancestors.insert(0, current)
		current = Element(u'table', {})
		yield START, current
		yield TEXT, u'\n\t'
		ancestors.insert(0, current)
		current = Element(u'tr', {u'class': u'greybg'})
		yield START, current
		yield TEXT, u'\n\t\t'
		ancestors.insert(0, current)
		current = Element(u'th', {u'style': u'width: 12em;'})
		yield START, current
		yield TEXT, u'Date'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t\t'
		ancestors.insert(0, current)
		current = Element(u'th', {u'style': u'width: 12em;'})
		yield START, current
		yield TEXT, u'Time'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t\t'
		ancestors.insert(0, current)
		current = Element(u'th', {u'style': u'width: 12em;'})
		yield START, current
		yield TEXT, u'Duration'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t'
		ancestors.insert(0, current)
		current = Element(u'tr', {})
		yield START, current
		yield TEXT, u'\n\t\t'
		_cont = date_field('started', session.started)
		ancestors.insert(0, current)
		current = Element(u'td', {u'style': u'text-align: center'})
		yield START, current
		for _e in template_util.generate_content(_cont):
			yield _e
			del _e
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t\t'
		_cont = time_field('started', session.started)
		ancestors.insert(0, current)
		current = Element(u'td', {u'style': u'text-align: center'})
		yield START, current
		for _e in template_util.generate_content(_cont):
			yield _e
			del _e
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t\t'
		_cont = duration_field('duration', session.duration)
		ancestors.insert(0, current)
		current = Element(u'td', {u'style': u'text-align: center'})
		yield START, current
		for _e in template_util.generate_content(_cont):
			yield _e
			del _e
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t'
		ancestors.insert(0, current)
		current = Element(u'tr', {u'class': u'greybg'})
		yield START, current
		yield TEXT, u'\n\t\t'
		ancestors.insert(0, current)
		current = Element(u'th', {u'colspan': u'3', u'style': u'width: 12em;'})
		yield START, current
		yield TEXT, u'Notes'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t'
		ancestors.insert(0, current)
		current = Element(u'tr', {})
		yield START, current
		yield TEXT, u'\n\t\t'
		ancestors.insert(0, current)
		current = Element(u'td', {u'colspan': u'3', u'style': u'text-align: center'})
		yield START, current
		yield TEXT, u'\n'
		ancestors.insert(0, current)
		current = Element(u'textarea', {u'rows': u'4', u'cols': u'70', u'name': u'notes'})
		yield START, current
		for _e in [session.notes]:
			for _e2 in template_util.generate_content(_e): yield _e2
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t\t'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t\n\t'
		ancestors.insert(0, current)
		current = Element(u'table', {})
		yield START, current
		yield TEXT, u'\n\t'
		ancestors.insert(0, current)
		current = Element(u'tr', {u'class': u'greybg'})
		yield START, current
		yield TEXT, u'\n\t\t'
		ancestors.insert(0, current)
		current = Element(u'th', {u'style': u'width: 16em;'})
		yield START, current
		yield TEXT, u'Name'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t\t'
		ancestors.insert(0, current)
		current = Element(u'th', {u'style': u'width: 20em;'})
		yield START, current
		yield TEXT, u'Settings'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t\t'
		ancestors.insert(0, current)
		current = Element(u'th', {})
		yield START, current
		yield TEXT, u'Loading'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t\t'
		ancestors.insert(0, current)
		current = Element(u'th', {})
		yield START, current
		yield TEXT, u'Duration'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t'
		results = dict([ (r.userMachine, r) for r in session.results ])
		yield TEXT, u'\n\t'
		for row, um in enumerate(user.userMachines):
			ancestors.insert(0, current)
			current = Element(u'tr', template_util.make_attrib({u'class': [rowclass[row%2]]}, self._get_assume_encoding()))
			yield START, current
			yield TEXT, u'\n\t\t'
			m, res = um.machine, results.get(um, None)
			if res:
				loading, duration = res.loading, res.duration
			else:
				loading, duration = None, None
			
			yield TEXT, u'\n\t\t'
			ancestors.insert(0, current)
			current = Element(u'input', template_util.make_attrib({u'type': u'hidden', u'name': u'userMachineID', u'value': [um.id]}, self._get_assume_encoding()))
			yield START, current
			yield END, current
			current = ancestors.pop(0)
			yield TEXT, u'\n\t\t'
			ancestors.insert(0, current)
			current = Element(u'td', {})
			yield START, current
			for _e in [m.name, u' - ', m.description]:
				for _e2 in template_util.generate_content(_e): yield _e2
			yield END, current
			current = ancestors.pop(0)
			yield TEXT, u'\n\t\t'
			_cont = um.settings or '-'
			ancestors.insert(0, current)
			current = Element(u'td', {u'style': u'white-space:pre'})
			yield START, current
			for _e in template_util.generate_content(_cont):
				yield _e
				del _e
			yield END, current
			current = ancestors.pop(0)
			yield TEXT, u'\n\t\t'
			ancestors.insert(0, current)
			current = Element(u'td', {})
			yield START, current
			yield TEXT, u'\n\t\t'
			ancestors.insert(0, current)
			current = Element(u'input', template_util.make_attrib({u'style': u'width: 1.6em', u'type': u'button', u'onclick': [u"incr('loading-", um.id, u"',-2)"], u'value': u'-'}, self._get_assume_encoding()))
			yield START, current
			yield END, current
			current = ancestors.pop(0)
			yield TEXT, u'\n\t\t'
			ancestors.insert(0, current)
			current = Element(u'input', template_util.make_attrib({u'style': u'text-align: center', u'name': [u'loading-', um.id], u'type': u'text', u'id': [u'loading-', um.id], u'value': [loading], u'size': u'7'}, self._get_assume_encoding()))
			yield START, current
			yield END, current
			current = ancestors.pop(0)
			yield TEXT, u'\n\t\t'
			ancestors.insert(0, current)
			current = Element(u'input', template_util.make_attrib({u'style': u'width: 1.6em', u'type': u'button', u'onclick': [u"incr('loading-", um.id, u"',+2)"], u'value': u'+'}, self._get_assume_encoding()))
			yield START, current
			yield END, current
			current = ancestors.pop(0)
			yield TEXT, u'\n\t\t'
			yield END, current
			current = ancestors.pop(0)
			yield TEXT, u'\n\t\t'
			ancestors.insert(0, current)
			current = Element(u'td', {})
			yield START, current
			yield TEXT, u'\n\t\t'
			ancestors.insert(0, current)
			current = Element(u'input', template_util.make_attrib({u'style': u'width: 1.6em', u'type': u'button', u'onclick': [u"incr('duration-", um.id, u"',-5)"], u'value': u'-'}, self._get_assume_encoding()))
			yield START, current
			yield END, current
			current = ancestors.pop(0)
			yield TEXT, u'\n\t\t'
			ancestors.insert(0, current)
			current = Element(u'input', template_util.make_attrib({u'style': u'text-align: center', u'name': [u'duration-', um.id], u'type': u'text', u'id': [u'duration-', um.id], u'value': [duration], u'size': u'7'}, self._get_assume_encoding()))
			yield START, current
			yield END, current
			current = ancestors.pop(0)
			yield TEXT, u'\n\t\t'
			ancestors.insert(0, current)
			current = Element(u'input', template_util.make_attrib({u'style': u'width: 1.6em', u'type': u'button', u'onclick': [u"incr('duration-", um.id, u"',+5)"], u'value': u'+'}, self._get_assume_encoding()))
			yield START, current
			yield END, current
			current = ancestors.pop(0)
			yield TEXT, u'\n\t\t'
			yield END, current
			current = ancestors.pop(0)
			yield TEXT, u'\n\t'
			yield END, current
			current = ancestors.pop(0)
		yield TEXT, u'\n\t'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t\n\t'
		ancestors.insert(0, current)
		current = Element(u'input', {u'type': u'submit', u'value': u'Save changes'})
		yield START, current
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\n'
		yield END, current
		current = ancestors.pop(0)
