#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Amol Kelkar'
SITENAME = "Amol's blog"
SITEURL = ''
SITETITLE = 'Amol Kelkar'
SITESUBTITLE = 'Artificial General Intelligence and Machine Consciousness Researcher'
SITEDESCRIPTION = 'Amol\'s Journey towards AGI and Machine Consciousness'
SITELOGO = None
BROWSER_COLOR = '#333'
ROBOTS = 'index, follow'

PATH = 'content'
THEME = 'themes/Flex'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']
IPYNB_USE_METACELL = True

