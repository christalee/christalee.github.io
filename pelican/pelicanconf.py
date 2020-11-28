#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Christalee Bieber'
SITENAME = 'Christalee Bieber - Teal Labs, Inc.'
SITEURL = ''
THEME = "theme/"
INDEX_SAVE_AS = "blog.html"

PATH = 'pelican/content'
ARTICLE_PATHS = ['posts']
ARTICLE_URL = "posts/{slug}.html"
ARTICLE_SAVE_AS = "posts/{slug}.html"
STATIC_PATHS = ['images', 'files']

MENUITEMS = (
    ('About', "/index.html#about"),
    ('Projects', "/index.html#projects"),
    ("Blog", "/blog.html"),
    ("Resume", "/pages/resume.html"),
)

TIMEZONE = 'America/New_York'
DEFAULT_DATE_FORMAT = '%d %B %Y'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'https://getpelican.com/'),
#          ('Python.org', 'https://www.python.org/'),
#          ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
LOAD_CONTENT_CACHE = False
