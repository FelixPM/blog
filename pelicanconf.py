#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = 'Félix Pérez Márquez'
SITENAME = AUTHOR
SITEURL = 'https://felixpm.cl'
SITETITLE = AUTHOR
SITESUBTITLE = 'Computer Scientist'
SITELOGO = "/images/profile.png"

PATH = 'content'
RELATIVE_URLS = False
TIMEZONE = 'America/Santiago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None



# Blogroll
LINKS = (('Pluralsight', 'https://app.pluralsight.com/profile/FelixPM'),
         ('Coursera', 'https://www.coursera.org/user/e31ef62fb3c3cd3b61aa1a782a9bd306'),
         ('Qwiklabs', 'https://www.qwiklabs.com/public_profiles/1d3676ac-6dcc-48ff-8418-30f227a3af8a'),
         )

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/felixpm15/'),
          ('github', 'https://github.com/FelixPM'),
          ('twitter', 'https://twitter.com/PerezMarquezF'),
          )


# MAIN_MENU = True
#
# MENUITEMS = (('Archive', '/archives.html'),
#              ('Categories', '/categories.html'))

DEFAULT_PAGINATION = False

THEME = "flex-theme"

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

STATIC_PATHS = ['images']

COPYRIGHT_YEAR = datetime.now().year

MARKUP = ("md", "ipynb")

from pelican_jupyter import markup as nb_markup
PLUGINS = [nb_markup]

IGNORE_FILES = [".ipynb_checkpoints"]
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True