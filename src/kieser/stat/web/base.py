# -*- coding: utf-8 -*-
# Kid template module
kid_version = '0.9.6'
kid_file = 'src/kieser/stat/web/base.kid'
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
from datetime import date, time, datetime
months = \
	"January February March April May June July " \
	"August September October November December"
months = dict( (i+1,m) for (i,m) in enumerate(months.split()) )
message = None
def date_field(*args, **kw):
	return Template().date_field(*args, **kw)
_def_names.append("date_field")
def time_field(*args, **kw):
	return Template().time_field(*args, **kw)
_def_names.append("time_field")
def duration_field(*args, **kw):
	return Template().duration_field(*args, **kw)
_def_names.append("duration_field")
def datetime_field(*args, **kw):
	return Template().datetime_field(*args, **kw)
_def_names.append("datetime_field")
class Template(BaseTemplate):
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
		yield TEXT, u'\n\n'
		yield TEXT, u'\n\n'
		yield TEXT, u'\n\n'
		yield TEXT, u'\n\n'
		yield TEXT, u'\n\n'
		yield TEXT, u'\n\n'
		yield END, current
		current = ancestors.pop(0)
	def _match_func(self, item, apply):
		exec template_util.get_locals(self, locals())
		current, ancestors = None, []
		ancestors.insert(0, current)
		current = Element(u'head', {})
		yield START, current
		yield TEXT, u'\n\t'
		titles = filter(lambda item: item.tag == 'title', item)
		if titles:
			title = titles[0]
			item.remove(title)
			title = title.text
		
		yield TEXT, u'\n\t'
		ancestors.insert(0, current)
		current = Element(u'title', {})
		yield START, current
		yield TEXT, u'\n\t\tKieser Training Customer Portal\n\t\t'
		if title:
			for _e in [u' - ', title]:
				for _e2 in template_util.generate_content(_e): yield _e2
		yield TEXT, u'\n\t'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t'
		ancestors.insert(0, current)
		current = Element(u'link', {u'href': u'kieser-icon.png', u'rel': u'shortcut icon'})
		yield START, current
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t'
		ancestors.insert(0, current)
		current = Element(u'link', {u'href': u'base.css', u'type': u'text/css', u'rel': u'stylesheet', u'title': u'Base styles'})
		yield START, current
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t'
		ancestors.insert(0, current)
		current = Element(u'script', {u'src': u'js/MochiKit/MochiKit.js', u'type': u'text/javascript'})
		yield START, current
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t'
		ancestors.insert(0, current)
		current = Element(u'script', {u'type': u'text/javascript'})
		yield START, current
		yield TEXT, u'\n\tvar loading = new Image();\n\tloading.src = "loading.gif";\n\t'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t'
		for node in item:
			_cont = node
			for _e in template_util.generate_content(_cont):
				yield _e
				del _e
		yield TEXT, u'\n'
		yield END, current
		current = ancestors.pop(0)
	_match_templates.append((lambda item: item.tag == '{http://www.w3.org/1999/xhtml}head', _match_func))
	def _match_func(self, item, apply):
		exec template_util.get_locals(self, locals())
		current, ancestors = None, []
		ancestors.insert(0, current)
		current = Element(u'body', {})
		yield START, current
		yield TEXT, u'\n\t'
		if user is not None:
			ancestors.insert(0, current)
			current = Element(u'div', {u'id': u'usernote'})
			yield START, current
			for _e in [user.surname, u', ', user.firstName]:
				for _e2 in template_util.generate_content(_e): yield _e2
			yield END, current
			current = ancestors.pop(0)
		yield TEXT, u'\n\t\n\t'
		ancestors.insert(0, current)
		current = Element(u'h1', {u'id': u'header'})
		yield START, current
		yield TEXT, u'\n\t\t'
		ancestors.insert(0, current)
		current = Element(u'img', {u'src': u'kieser-logo.gif', u'alt': u'Kieser Training logo'})
		yield START, current
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t\tKieser Training Customer Portal\n\t'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t\n\t'
		ancestors.insert(0, current)
		current = Element(u'div', {u'id': u'menubar'})
		yield START, current
		yield TEXT, u'\n\t\t'
		for node in item.findall('menubar/a'):
			_cont = node
			for _e in template_util.generate_content(_cont):
				yield _e
				del _e
		yield TEXT, u'\n\t\t'
		if user is not None:
			ancestors.insert(0, current)
			current = Element(u'a', template_util.make_attrib({u'href': [this, u'/logout']}, self._get_assume_encoding()))
			yield START, current
			yield TEXT, u'Logout '
			ancestors.insert(0, current)
			current = Element(u'strong', {})
			yield START, current
			for _e in [user.userID]:
				for _e2 in template_util.generate_content(_e): yield _e2
			yield END, current
			current = ancestors.pop(0)
			yield END, current
			current = ancestors.pop(0)
		yield TEXT, u'\n\t'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t\n\t'
		ancestors.insert(0, current)
		current = Element(u'div', {u'id': u'content'})
		yield START, current
		yield TEXT, u'\n\t\t'
		if message:
			ancestors.insert(0, current)
			current = Element(u'p', {u'style': u'color:red'})
			yield START, current
			for _e in [message]:
				for _e2 in template_util.generate_content(_e): yield _e2
			yield END, current
			current = ancestors.pop(0)
		yield TEXT, u'\n\t\t'
		for node in item.findall('content/*'):
			_cont = node
			for _e in template_util.generate_content(_cont):
				yield _e
				del _e
		yield TEXT, u'\n\t'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t\n'
		yield END, current
		current = ancestors.pop(0)
	_match_templates.append((lambda item: item.tag == '{http://www.w3.org/1999/xhtml}body', _match_func))
	def __date_field(self, name, dt):
		exec template_util.get_locals(self, locals())
		current, ancestors = None, []
		yield TEXT, u'\n\t'
		ancestors.insert(0, current)
		current = Element(u'span', {u'style': u'white-space: nowrap'})
		yield START, current
		yield TEXT, u'\n\t\t'
		ancestors.insert(0, current)
		current = Element(u'select', template_util.make_attrib({u'name': [name, u'-day']}, self._get_assume_encoding()))
		yield START, current
		yield TEXT, u'\n\t\t'
		for day in range(1,32):
			ancestors.insert(0, current)
			current = Element(u'option', template_util.make_updated_attrib({}, "(day == dt.day) and {'selected':'selected'} or {}", globals(), locals(), self._get_assume_encoding()))
			yield START, current
			for _e in ['%02d' % day]:
				for _e2 in template_util.generate_content(_e): yield _e2
			yield END, current
			current = ancestors.pop(0)
		yield TEXT, u'\n\t\t'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t\t'
		ancestors.insert(0, current)
		current = Element(u'select', template_util.make_attrib({u'name': [name, u'-month']}, self._get_assume_encoding()))
		yield START, current
		yield TEXT, u'\n\t\t'
		for month in range(1,13):
			ancestors.insert(0, current)
			current = Element(u'option', template_util.make_updated_attrib({u'value': [month]}, "(month == dt.month) and {'selected':'selected'} or {}", globals(), locals(), self._get_assume_encoding()))
			yield START, current
			for _e in [months[month]]:
				for _e2 in template_util.generate_content(_e): yield _e2
			yield END, current
			current = ancestors.pop(0)
		yield TEXT, u'\n\t\t'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t\t'
		ancestors.insert(0, current)
		current = Element(u'select', template_util.make_attrib({u'name': [name, u'-year']}, self._get_assume_encoding()))
		yield START, current
		yield TEXT, u'\n\t\t'
		for year in range(2000,datetime.now().year+1):
			ancestors.insert(0, current)
			current = Element(u'option', template_util.make_updated_attrib({}, "(year == dt.year) and {'selected':'selected'} or {}", globals(), locals(), self._get_assume_encoding()))
			yield START, current
			for _e in [year]:
				for _e2 in template_util.generate_content(_e): yield _e2
			yield END, current
			current = ancestors.pop(0)
		yield TEXT, u'\n\t\t'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n'
	def date_field(self, *args, **kw):
		return ElementStream(self.__date_field(*args, **kw))
	def __time_field(self, name, dt):
		exec template_util.get_locals(self, locals())
		current, ancestors = None, []
		yield TEXT, u'\n\t'
		ancestors.insert(0, current)
		current = Element(u'span', {u'style': u'white-space: nowrap'})
		yield START, current
		yield TEXT, u'\n\t\t'
		ancestors.insert(0, current)
		current = Element(u'select', template_util.make_attrib({u'name': [name, u'-hour']}, self._get_assume_encoding()))
		yield START, current
		yield TEXT, u'\n\t\t'
		for hour in range(0,24):
			ancestors.insert(0, current)
			current = Element(u'option', template_util.make_updated_attrib({}, "(hour == dt.hour) and {'selected':'selected'} or {}", globals(), locals(), self._get_assume_encoding()))
			yield START, current
			for _e in ['%02d' % hour]:
				for _e2 in template_util.generate_content(_e): yield _e2
			yield END, current
			current = ancestors.pop(0)
		yield TEXT, u'\n\t\t'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t\t'
		ancestors.insert(0, current)
		current = Element(u'select', template_util.make_attrib({u'name': [name, u'-minute']}, self._get_assume_encoding()))
		yield START, current
		yield TEXT, u'\n\t\t'
		for minute in range(0,60,5):
			ancestors.insert(0, current)
			current = Element(u'option', template_util.make_updated_attrib({}, "(minute <= dt.minute < minute+5) and {'selected':'selected'} or {}", globals(), locals(), self._get_assume_encoding()))
			yield START, current
			for _e in ['%02d' % minute]:
				for _e2 in template_util.generate_content(_e): yield _e2
			yield END, current
			current = ancestors.pop(0)
		yield TEXT, u'\n\t\t'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n\t'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n'
	def time_field(self, *args, **kw):
		return ElementStream(self.__time_field(*args, **kw))
	def __duration_field(self, name, dt):
		exec template_util.get_locals(self, locals())
		current, ancestors = None, []
		yield TEXT, u'\n\t'
		ancestors.insert(0, current)
		current = Element(u'span', {u'style': u'white-space: nowrap'})
		yield START, current
		yield TEXT, u'\n\t\t'
		if isinstance(dt, basestring):
			hours, minutes = map(int, dt.split(":"))
		else:
			hours, seconds = divmod(dt.seconds, 3600)
			hours += (dt.days * 24)
			minutes = seconds // 60
		
		yield TEXT, u'\n\t\t'
		ancestors.insert(0, current)
		current = Element(u'select', template_util.make_attrib({u'name': [name, u'-hours']}, self._get_assume_encoding()))
		yield START, current
		yield TEXT, u'\n\t\t'
		for hour in range(0,5):
			ancestors.insert(0, current)
			current = Element(u'option', template_util.make_updated_attrib({}, "(hour == hours) and {'selected':'selected'} or {}", globals(), locals(), self._get_assume_encoding()))
			yield START, current
			for _e in [hour]:
				for _e2 in template_util.generate_content(_e): yield _e2
			yield END, current
			current = ancestors.pop(0)
		yield TEXT, u'\n\t\t'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u' hours\n\t\t'
		ancestors.insert(0, current)
		current = Element(u'select', template_util.make_attrib({u'name': [name, u'-minutes']}, self._get_assume_encoding()))
		yield START, current
		yield TEXT, u'\n\t\t'
		for minute in range(0,60,5):
			ancestors.insert(0, current)
			current = Element(u'option', template_util.make_updated_attrib({}, "(minute <= minutes < minute+5) and {'selected':'selected'} or {}", globals(), locals(), self._get_assume_encoding()))
			yield START, current
			for _e in ['%02d' % minute]:
				for _e2 in template_util.generate_content(_e): yield _e2
			yield END, current
			current = ancestors.pop(0)
		yield TEXT, u'\n\t\t'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u' minutes\n\t'
		yield END, current
		current = ancestors.pop(0)
		yield TEXT, u'\n'
	def duration_field(self, *args, **kw):
		return ElementStream(self.__duration_field(*args, **kw))
	def __datetime_field(self, name, dt):
		exec template_util.get_locals(self, locals())
		current, ancestors = None, []
		yield TEXT, u'\n\t'
		_cont = date_field(name, dt)
		for _e in template_util.generate_content(_cont):
			yield _e
			del _e
		yield TEXT, u'\n\t'
		_cont = time_field(name, dt)
		for _e in template_util.generate_content(_cont):
			yield _e
			del _e
		yield TEXT, u'\n'
	def datetime_field(self, *args, **kw):
		return ElementStream(self.__datetime_field(*args, **kw))
