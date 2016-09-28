# -*- coding: utf-8 -*-
# Kid template module
kid_version = '0.9.6'
kid_file = 'src/kieser/stat/web/sessions.kid'
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
		yield TEXT, u'Sessions'
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
		yield TEXT, u'Sessions'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t\n\t'
		ancestors.insert(0, current)
		current = Element(u'form', template_util.make_attrib({u'action': [req.uri], u'accept-charset': u'UTF-8', u'method': u'POST'}, self._get_assume_encoding()))
		yield START, current
		yield TEXT, u'\n\t'
		ancestors.insert(0, current)
		current = Element(u'div', {})
		yield START, current
		ancestors.insert(0, current)
		current = Element(u'input', {u'type': u'submit', u'name': u'new', u'value': u'New session'})
		yield START, current
		yield END, current
		current = ancestors.pop(0)
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t\n\t'
		ancestors.insert(0, current)
		current = Element(u'table', {u'style': u'margin-top: 0.5em'})
		yield START, current
		yield TEXT, u'\n\t'
		ancestors.insert(0, current)
		current = Element(u'tr', {u'class': u'greybg'})
		yield START, current
		yield TEXT, u'\n\t\t'
		ancestors.insert(0, current)
		current = Element(u'th', {})
		yield START, current
		yield TEXT, u'Date'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t\t'
		ancestors.insert(0, current)
		current = Element(u'th', {})
		yield START, current
		yield TEXT, u'Day'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t\t'
		ancestors.insert(0, current)
		current = Element(u'th', {})
		yield START, current
		yield TEXT, u'Time'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t\t'
		ancestors.insert(0, current)
		current = Element(u'th', {})
		yield START, current
		yield TEXT, u'Duration'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t\t'
		ancestors.insert(0, current)
		current = Element(u'th', {})
		yield START, current
		yield TEXT, u'Notes'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t\t'
		ancestors.insert(0, current)
		current = Element(u'th', {})
		yield START, current
		yield TEXT, u'Actions'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t'
		sessions = user.sessions
		def key(session): return session.started
		sessions.sort(key=key, reverse=True)
		rowclass = "even", "odd"
		
		yield TEXT, u'\n\t'
		for row, session in enumerate(sessions):
			ancestors.insert(0, current)
			current = Element(u'tr', template_util.make_attrib({u'class': [rowclass[row%2]]}, self._get_assume_encoding()))
			yield START, current
			yield TEXT, u'\n\t\t'
			_cont = session.started.strftime('%d %B %Y')
			ancestors.insert(0, current)
			current = Element(u'td', {u'style': u'text-align: center'})
			yield START, current
			for _e in template_util.generate_content(_cont):
				yield _e
				del _e
			yield END, current
			current = ancestors.pop(0)
			yield TEXT, u'\n\t\t'
			_cont = session.started.strftime('%A')
			ancestors.insert(0, current)
			current = Element(u'td', {u'style': u'text-align: center'})
			yield START, current
			for _e in template_util.generate_content(_cont):
				yield _e
				del _e
			yield END, current
			current = ancestors.pop(0)
			yield TEXT, u'\n\t\t'
			_cont = session.started.strftime('%H:%M')
			ancestors.insert(0, current)
			current = Element(u'td', {u'style': u'text-align: center'})
			yield START, current
			for _e in template_util.generate_content(_cont):
				yield _e
				del _e
			yield END, current
			current = ancestors.pop(0)
			yield TEXT, u'\n\t\t'
			duration = session.duration
			if duration:
				hours, seconds = divmod(duration.seconds, 3600)
				minutes = seconds/60
				if hours and minutes:
					duration = "%d hour%s %d mins" % (
						hours, (not hours == 1) and 's' or '', minutes,
					)
				elif hours:
					duration = "%d hour%s" % (
						hours, (not hours == 1) and 's' or '',
					)
				else:
					duration = "%d mins" % minutes
			
			yield TEXT, u'\n\t\t'
			_cont = duration or '-'
			ancestors.insert(0, current)
			current = Element(u'td', {u'style': u'text-align: center'})
			yield START, current
			for _e in template_util.generate_content(_cont):
				yield _e
				del _e
			yield END, current
			current = ancestors.pop(0)
			yield TEXT, u'\n\t\t'
			_cont = session.notes or '-'
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
			current = Element(u'td', {u'style': u'text-align: center'})
			yield START, current
			yield TEXT, u'\n\t\t\t'
			ancestors.insert(0, current)
			current = Element(u'form', template_util.make_attrib({u'action': [req.uri], u'accept-charset': u'UTF-8', u'method': u'GET'}, self._get_assume_encoding()))
			yield START, current
			yield TEXT, u'\n\t\t\t'
			ancestors.insert(0, current)
			current = Element(u'div', {})
			yield START, current
			yield TEXT, u'\n\t\t\t'
			ancestors.insert(0, current)
			current = Element(u'input', template_util.make_attrib({u'type': u'hidden', u'name': u'edit', u'value': [session.id]}, self._get_assume_encoding()))
			yield START, current
			yield END, current
			current = ancestors.pop(0)
			yield TEXT, u'\n\t\t\t'
			ancestors.insert(0, current)
			current = Element(u'input', {u'type': u'submit', u'value': u'Edit'})
			yield START, current
			yield END, current
			current = ancestors.pop(0)
			yield TEXT, u'\n\t\t\t'
			yield END, current
			current = ancestors.pop(0)
			yield TEXT, u'\n\t\t\t'
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
		yield TEXT, u'\n\t\n'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\n'
		yield END, current
		current = ancestors.pop(0)
