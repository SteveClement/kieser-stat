# -*- coding: utf-8 -*-
# Kid template module
kid_version = '0.9.6'
kid_file = 'src/kieser/stat/web/error.kid'
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
title, error = "Error", None
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
		yield TEXT, u'\n'
		ancestors.insert(0, current)
		current = Element(u'head', {})
		yield START, current
		yield TEXT, u'\n\t'
		_cont = title
		ancestors.insert(0, current)
		current = Element(u'title', {})
		yield START, current
		for _e in template_util.generate_content(_cont):
			yield _e
			del _e
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t'
		ancestors.insert(0, current)
		current = Element(u'style', {u'type': u'text/css'})
		yield START, current
		yield TEXT, u'\n\t\t#content {\n\t\t\tborder-left: 5px solid red;\n\t\t\tpadding-left: 1em;\n\t\t}\n\t\t#message {\n\t\t\tfont-size: larger;\n\t\t}\n\t'
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
		if error:
			_cont = error
			ancestors.insert(0, current)
			current = Element(u'p', {u'id': u'message'})
			yield START, current
			for _e in template_util.generate_content(_cont):
				yield _e
				del _e
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
