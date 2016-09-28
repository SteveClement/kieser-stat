from distutils.core import setup
from os.path import dirname, join
from glob import glob
import sys

sys.path.insert(0, join(dirname(__file__), "src"))

name = 'kieser-stat'
from kieser.stat import __version__ as version
description = """\
Tools for allowing customers of a gym to store their machine settings, session times
and session results in a database. The customers and staff can then analyse the
database to monitor progress."""

setup(
	name=name,
	description=description,
	version=version,
	author='Gavin Panella',
	author_email='gavin@ion.lu',
	url='http://www.ion.lu/',
	packages=['kieser','kieser.stat','kieser.stat.web'],
	package_dir={'kieser': 'src/kieser'},
	package_data={'kieser.stat.web': ['*.kid']},
	data_files=[
		#('share/%s-%s/bin' % (name, version), glob('bin/*')),
		('share/%s-%s/misc' % (name, version), glob('misc/*')),
	],
)
