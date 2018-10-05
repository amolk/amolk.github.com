#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Amol Kelkar'
SITENAME = "Amol's blog"
SITEURL = 'https://amolk.github.io'
SITETITLE = 'Amol Kelkar'
SITESUBTITLE = 'Artificial General Intelligence and Machine Consciousness Researcher'
SITEDESCRIPTION = 'Amol\'s Journey towards AGI and Machine Consciousness'
SITELOGO = '/images/profile.png'
BROWSER_COLOR = '#333'
ROBOTS = 'index, follow'

PATH = 'content'
THEME = 'themes/Flex'
STATIC_PATHS = ['images', 'css']
IGNORE_FILES = ['.ipynb_checkpoints']
EXTRA_PATH_METADATA = {
    'css/custom.css': {'path': 'css/custom.css'},
}
CUSTOM_CSS = 'css/custom.css'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
AUTHOR_FEED_RSS = 'feeds/%s.rss.xml'
RSS_FEED_SUMMARY_ONLY = False

# Blogroll
LINKS = (('LinkedIn', 'https://www.linkedin.com/in/amol-kelkar/'),)

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/amol-kelkar/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
MARKUP = ('md', 'ipynb', 'render_math')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']
IPYNB_USE_METACELL = True

