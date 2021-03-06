# coding: utf-8
from __future__ import absolute_import

import os
import sys

from gi.repository import Gtk, Gdk, Pango
from collections import namedtuple


Contributor = namedtuple(
				'Contributor',
				[
					'name',  # contributor's full name
					'email',
					'website',  # contributor's website url
				])


class AboutWindow:
	# list of contributors
	contributors = [
		Contributor(
			name = 'Mladen Mijatov',
			email = 'meaneye.rcf@gmail.com',
			website = None,
		),
		Contributor(
			name = 'Wojciech Kluczka',
			email = 'wojtekkluczka@gmail.com',
			website = None,
		),
		Contributor(
			name = 'Grigory Petrov',
			email = 'grigory.v.p@gmail.com',
			website = None,
		),
		Contributor(
			name = 'Sebastian Gaul',
			email = 'sebastian@dev.mgvmedia.com',
			website = 'http://sgaul.de',
		),
		Contributor(
			name = 'Arseniy Krasnov ',
			email = 'arseniy@krasnoff.org',
			website = None,
		),
		Contributor(
			name = 'Sevka Fedoroff',
			email = 'sevka.fedoroff@gmail.com',
			website = None
		),
		Contributor(
			name = 'multiSnow',
			email = 'infinity.blick.winkel@gmail.com',
			website = None
		)
	]

	# list of artists
	artists = [
		Contributor(
			name = 'Andrea Pavlović',
			email = 'octogirl.design@gmail.com',
			website = None,
		),
		Contributor(
			name = 'Michael Kerch',
			email = 'michael@way2cu.com',
			website = 'https://misha.co.il',
		),
	]

	translators = [

	]

	def __init__(self, parent):
		# create main window
		self._dialog = Gtk.AboutDialog()

		# prepare version template
		if parent.version['stage'] != 'f':
			version = '{0[major]}.{0[minor]}{0[stage]} ({0[build]})'.format(parent.version)
		else:
			version = '{0[major]}.{0[minor]} ({0[build]})'.format(parent.version)

		# add Python version info
		version += '\n\nPython {}.{}.{}'.format(*sys.version_info[:3])
		version += '\nGtk+ {}.{}.{}'.format(Gtk.MAJOR_VERSION, Gtk.MINOR_VERSION, Gtk.MICRO_VERSION)

		# set about dialog image
		base_path = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))
		image_path = os.path.join(base_path, 'images', 'splash.png')
		path = os.path.abspath(image_path)

		image = Gtk.Image()
		image.set_from_file(path)

		# configure dialog
		self._dialog.set_modal(True)
		self._dialog.set_transient_for(parent)
		self._dialog.set_wmclass('Sunflower', 'Sunflower')

		# connect signals
		self._dialog.connect('activate-link', parent.goto_web)

		# set dialog data
		self._dialog.set_name(_('Sunflower'))
		self._dialog.set_program_name(_('Sunflower'))
		self._dialog.set_version(version)
		self._dialog.set_logo(image.get_pixbuf())
		self._dialog.set_website('sunflower-fm.org')
		self._dialog.set_comments(_('Twin-panel file manager for Linux.'))

		# set license
		self._dialog.set_copyright(_(u'Copyright \u00a9 2010-2018 by Mladen Mijatov and contributors.'))

		license_file = os.path.join(base_path, 'COPYING')
		if os.path.isfile(license_file):
			license_file = open(license_file, 'r')

			if license_file:
				license_text = license_file.read()
				license_file.close()

				self._dialog.set_license(license_text)

		else:
			# link to GPL3
			self._dialog.set_license('http://www.gnu.org/licenses/old-licenses/gpl-3.0.html')

		# set authors
		self._dialog.set_authors(['{0} <{1}> {2}'.format(
					contributor.name,
					contributor.email,
					(u'\xa0<a href="{0}">{0}</a>'.format(contributor.website) if contributor.website else '')
				) for contributor in self.contributors])

		self._dialog.set_artists(['{0} <{1}> {2}'.format(
					contributor.name,
					contributor.email,
					(u'\xa0<a href="{0}">{0}</a>'.format(contributor.website) if contributor.website else '')
				) for contributor in self.artists])

		self._dialog.set_translator_credits('\n'.join(['{0} <{1}> {2} - {3}'.format(
					contributor.name,
					contributor.email,
					(u'\xa0<a href="{0}">{0}</a>'.format(contributor.website) if contributor.website else ''),
					contributor.language
				) for contributor in self.translators]))

	def show(self):
		"""Show dialog"""
		self._dialog.run()
		self._dialog.destroy()
