#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'PMLG'
SITENAME = 'Perth Machine Learning Group'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Australia/Perth'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Fast.ai', 'http://fast.ai/'),)

# Social widget
SOCIAL = (('GitHub', 'http://github.com/pmlg/'),)

DEFAULT_PAGINATION = 4

EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

THEME='themes/Flex/'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
