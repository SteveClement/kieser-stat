# -*- coding: utf-8 -*-
# Kid template module
kid_version = '0.9.6'
kid_file = 'src/kieser/stat/web/login.kid'
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
goingto = None
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
		yield TEXT, u'Login'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t'
		ancestors.insert(0, current)
		current = Element(u'style', {u'type': u'text/css'})
		yield START, current
		yield TEXT, u'\n\t\t#content td { text-align: right; }\n\t'
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
		current = Element(u'content', {})
		yield START, current
		yield TEXT, u'\n\t'
		ancestors.insert(0, current)
		current = Element(u'form', template_util.make_attrib({u'action': [this, u'/login'], u'accept-charset': u'UTF-8', u'method': u'POST'}, self._get_assume_encoding()))
		yield START, current
		yield TEXT, u'\n\t'
		if goingto is not None:
			ancestors.insert(0, current)
			current = Element(u'input', template_util.make_attrib({u'type': u'hidden', u'value': [goingto], u'name': u'goingto'}, self._get_assume_encoding()))
			yield START, current
			yield END, current
			current = ancestors.pop(0)
		yield TEXT, u'\n\t'
		ancestors.insert(0, current)
		current = Element(u'table', {})
		yield START, current
		yield TEXT, u'\n\t'
		ancestors.insert(0, current)
		current = Element(u'tr', {})
		yield START, current
		yield TEXT, u'\n\t\t'
		ancestors.insert(0, current)
		current = Element(u'td', {})
		yield START, current
		ancestors.insert(0, current)
		current = Element(u'label', {u'for': u'userID'})
		yield START, current
		yield TEXT, u'User name:'
		yield END, current
		current = ancestors.pop(0)
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t\t'
		ancestors.insert(0, current)
		current = Element(u'td', {})
		yield START, current
		ancestors.insert(0, current)
		current = Element(u'input', {u'name': u'userID', u'tabindex': u'1', u'type': u'text', u'id': u'userID', u'value': u'steve', u'size': u'20'})
		yield START, current
		yield END, current
		current = ancestors.pop(0)
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t\t'
		ancestors.insert(0, current)
		current = Element(u'td', {u'rowspan': u'2'})
		yield START, current
		ancestors.insert(0, current)
		current = Element(u'input', {u'style': u'display:block; height:100%', u'type': u'submit', u'name': u'login', u'value': u'Log-in'})
		yield START, current
		yield END, current
		current = ancestors.pop(0)
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
		ancestors.insert(0, current)
		current = Element(u'label', {u'for': u'password'})
		yield START, current
		yield TEXT, u'Password:'
		yield END, current
		current = ancestors.pop(0)
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t\t'
		ancestors.insert(0, current)
		current = Element(u'td', {})
		yield START, current
		ancestors.insert(0, current)
		current = Element(u'input', {u'name': u'password', u'tabindex': u'1', u'type': u'password', u'id': u'password', u'value': u'foobar', u'size': u'20'})
		yield START, current
		yield END, current
		current = ancestors.pop(0)
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t'
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
