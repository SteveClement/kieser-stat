# -*- coding: utf-8 -*-
# Kid template module
kid_version = '0.9.6'
kid_file = 'src/kieser/stat/web/user_machine_edit.kid'
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
		yield TEXT, u'User Machines'
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
		machine = user_machine.machine
		yield TEXT, u'\n\t\n\t'
		ancestors.insert(0, current)
		current = Element(u'h2', {})
		yield START, current
		for _e in [u'Editing machine ', machine.name, u' - ', machine.description]:
			for _e2 in template_util.generate_content(_e): yield _e2
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t\n\t'
		ancestors.insert(0, current)
		current = Element(u'form', template_util.make_attrib({u'action': [req.uri], u'accept-charset': u'UTF-8', u'method': u'POST'}, self._get_assume_encoding()))
		yield START, current
		yield TEXT, u'\n\t'
		ancestors.insert(0, current)
		current = Element(u'input', template_util.make_attrib({u'type': u'hidden', u'name': u'update', u'value': [user_machine.id]}, self._get_assume_encoding()))
		yield START, current
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t'
		ancestors.insert(0, current)
		current = Element(u'table', {u'id': u'user-machines'})
		yield START, current
		yield TEXT, u'\n\t'
		ancestors.insert(0, current)
		current = Element(u'tr', {u'class': u'greybg'})
		yield START, current
		yield TEXT, u'\n\t\t'
		ancestors.insert(0, current)
		current = Element(u'th', {u'style': u'width: 24em;'})
		yield START, current
		yield TEXT, u'Settings'
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
		current = Element(u'td', {})
		yield START, current
		yield TEXT, u'\n'
		ancestors.insert(0, current)
		current = Element(u'textarea', {u'rows': u'7', u'cols': u'55', u'id': u'settings', u'name': u'settings'})
		yield START, current
		for _e in [user_machine.settings]:
			for _e2 in template_util.generate_content(_e): yield _e2
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n'
		ancestors.insert(0, current)
		current = Element(u'script', {u'type': u'text/javascript'})
		yield START, current
		yield TEXT, u"focusOnLoad('settings');"
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
		yield TEXT, u'\n\t'
		ancestors.insert(0, current)
		current = Element(u'input', {u'type': u'submit', u'value': u'Save changes'})
		yield START, current
		yield END, current
		current = ancestors.pop(0)
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
