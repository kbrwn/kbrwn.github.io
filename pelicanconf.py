#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Kyle Brown'
SITENAME = u'kbrwn'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

THEME = "/Users/kyle/pelican-themes/svbhack"
STATIC_PATHS = ['images', ]
USER_LOGO_URL = '/images/index.jpg'
TAGLINE = 'junior sysadmin. pythonista.'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
# Blogroll
#LINKS = (,)

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/ky1e0/'),
          ('GitHub', 'http://github.com/kbrwn'),
          ('Linkedin', 'http://linkedin.com/in/kbrwn'))

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
