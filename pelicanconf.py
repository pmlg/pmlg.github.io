#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'PMLG'
SITENAME = 'Perth Machine Learning Group'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Australia/Perth'

DEFAULT_LANG = 'English'

SITESUBTITLE = "Perth's Machine Learning Group"

SITEDESCRIPTION = "We are a group of students, industry professionals, entrepreneurs and curious individuals studying machine learning. We run beginner and advanced sessions every Thursday from 6-8pm at Flux, 191 St George's Terrace."

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Join Our Mailing List','https://groups.google.com/d/forum/perthdeeplearners'),
    ('Deep Learning Course Material', 'http://course.fast.ai/'),
)

# Social widget
SOCIAL = (('GitHub', 'http://github.com/pmlg/'),)

DEFAULT_PAGINATION = 4

STATIC_PATHS = ['images','extra']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

THEME='themes/Flex/'
PLUGIN_PATH=['../pelican-plugins/']
PLUGINS = ['events']
PLUGIN_EVENTS = {
    'ics_fname': 'calendar.ics',
}


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
