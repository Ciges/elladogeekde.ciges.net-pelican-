#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ciges'
AUTHOR_COMPLETE_NAME = "José Manuel Ciges Regueiro"
SITENAME = '¡Comparte, insensato!'
SITESUBTITLE = "el lado geek de Ciges"
# Producción
SITEURL = 'http://elladogeekde.ciges.net'
# Desarrollo
#SITEURL = "http://localhost"
DESCRIPTION = "Reflexiones de un informático de sistemas de la generación del 76, enamorado del software libre, vigués, padre y algo bohemio y soñador entre otras cosas"

#USER_LOGO_URL = SITEURL + "/theme/images/logo.png"
USER_LOGO_URL = SITEURL + "/theme/images/ciges.png"

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

## Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)
#
## Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Configuración personalizada
STATIC_PATHS = ['images', 'docs' ]
ARTICLE_URL = '{category}/{slug}'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'
#THEME="hyde"
#THEME="/var/www/elladogeekde.ciges.net/themes/notmyidea_custom"
THEME="/var/www/elladogeekde.ciges.net/themes/svbhack_custom"
PLUGIN_PATHS = [ "/var/www/elladogeekde.ciges.net/plugins" ]
PLUGINS = [ "optimize_images", "better_figures_and_images", "liquid_tags.img", "assets" ]

# Comentarios con Disqus
DISQUS_SITENAME = "elladogeekdeciges"

# Enlaces a las redes sociales
SOCIAL = (
            ('Facebook', 'http://www.facebook.com/ciges'),
            ('Twitter', 'http://twitter.com/Ciges'),
            ('Email', 'mailto://jmanuel@ciges.net'),
            ('LinkedIn', 'http://es.linkedin.com/in/jmciges'),
        )

# Analíticas con Google Analytics (Universal Analytics)
GOOGLE_ANALYTICS = "UA-74045349-1";

# Si es False no usamos recursos de Internet (fuentes de Google, comentarios con Disqus, compartir con AddThis)
CONEXION_INTERNET = True
