# -*- coding: utf-8 -*-
import os
_ = lambda s: s

DEBUG = False
TEMPLATE_DEBUG = DEBUG
BASICAUTH_ACTIVE = False

SECRET_KEY = ')$(t@r&rmly$5k)%8uxpf%=72@f!4=ol+h-0dw4!7xr!8f+52!'

SITE_ID = 1
ROOT_URLCONF = 'urls'

SRC_ROOT = os.path.dirname(__file__)
PROJECT_ROOT = os.path.join(SRC_ROOT, '..')
DATA_ROOT = os.environ.get('DATA_ROOT', os.path.join(PROJECT_ROOT, 'tmp'))
MEDIA_ROOT = os.path.join(DATA_ROOT, 'media')
STATIC_ROOT = os.path.join(DATA_ROOT, 'static_collected')

MEDIA_URL = '/media/'
STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = ''.join([STATIC_URL, 'admin/'])
STATICFILES_DIRS = [os.path.join(PROJECT_ROOT, 'static')]
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'core.staticfiles_finders.AppDirectoriesFinderAsMedia',
    'compressor.finders.CompressorFinder',
]

LOCALE_PATHS = [
    os.path.join(PROJECT_ROOT, 'locale'),
]

# databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DATA_ROOT, 'db.sqlite3'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        }
}


# template related
TEMPLATE_DIRS = [os.path.join(PROJECT_ROOT, 'templates')]
SEKIZAI_IGNORE_VALIDATION = True  # Silence the whining!
TEMPLATE_LOADERS = [
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
]


# emails
SERVER_EMAIL = 'django@%s' % os.uname()[1]
ADMINS = (
    # ('Your Name', 'your_email@domain.com'),  # exception mails are handled by sentry
)
MANAGERS = ADMINS

DEFAULT_FROM_EMAIL = 'norepy@divio.ch'

# i18n, timezones and formatting
TIME_ZONE = 'Europe/Zurich'
USE_TZ = True
LANGUAGE_CODE = 'en'
USE_I18N = True
USE_L10N = True
DATE_FORMAT = 'd.m.Y'
DATETIME_FORMAT = 'd.m.Y H:i'
TIME_FORMAT = 'H:i'
YEAR_MONTH_FORMAT = 'F Y'
MONTH_DAY_FORMAT = 'j. F'
LANGUAGES = (
    ('de',    _('German')),
    ('en',    _('English')),
)

CMS_LANGUAGES = {
    # SITE_ID: [LANGUAGE_CODE_LIST]
    1: [
        {
            'code': 'de',
            'name': _('German'),
        },
        {
            'code': 'en',
            'name': _('English'),
        },
    ],
    'default': {
        'fallbacks': ['en', 'de'],
        'redirect_on_fallback': False,
        'public': True,
        'hide_untranslated': False,
    }
}

# apps, middlewares, templatecontext, authentication backends
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'djangocms_admin_style',  # must be before admin to override base template
    'admin_shortcuts',
    'django.contrib.admin',

    # cms plugins
    'cmsplugin_filer_file',
    'cmsplugin_filer_image',
    'cmsplugin_filer_folder',

    'djangocms_text_ckeditor',
    'djangocms_link',
    'djangocms_flash',
    'djangocms_snippet',

    # apps
    'aldryn_snake',
    'aldryn_style',
    'aldryn_grid_bootstrap',

    # 3rd party
    'gunicorn',
    'compressor',
    'south',
    'easy_thumbnails',
    'login_as',
    'standard_form',
    'robots',
    'django_commontranslations',
    # 'djcelery',  # uncomment for django-celery specific models

    # Health Check
    'health_check',
    # 'health_check_celery',
    'health_check_db',
    'health_check_cache',
    'health_check_storage',

    # cms related
    'cms',
    'mptt',
    'menus',
    'sekizai',
    'filer',
    'siteinfo',
    'reversion',

    # project
    'core',
    'aldryn_theme_autofaszination',
]

TEMPLATE_CONTEXT_PROCESSORS = [
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.debug',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'cms.context_processors.media',
    'siteinfo.context_processors.siteinfo',
    'django.core.context_processors.static',
    'sekizai.context_processors.sekizai',
    'aldryn_snake.template_api.template_processor',
]

MIDDLEWARE_CLASSES = [
    'core.middleware.BasicAuthMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'core.middleware.CurrentSiteMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'siteinfo.middleware.login_required.RequireLoginMiddleware',
    'core.utils.compatibility.XUACompatibleMiddleware',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'login_as.auth_backend.LoginAsBackend',
]

# Images / Thumbnailing
THUMBNAIL_BASEDIR = 'tmp'
THUMBNAIL_QUALITY = 95
THUMBNAIL_PRESERVE_EXTENSIONS = ['png']
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
    #'shop_plugnplay.utils.thumbnail_processors.whitespace',
)


# CMS
CMS_TEMPLATES = [
    ('fullwidth.html', _('full width')),
    ('sidebar_left.html', _('sidebar left')),
    ('sidebar_right.html', _('sidebar right')),
    ('tpl_home.html', _('home')),
]
CMS_PLACEHOLDER_CONF = {
    'content': {
        'plugins': (),
        'name': _('Primary'),
        'extra_context': {},
    },

    'feature': {
        'plugins': (),
        'name': _('Feature'),
        'extra_context': {},
    },
}

CMS_PAGE_MEDIA_PATH = 'uploads/cms_page_media/'
CMS_SOFTROOT = True
CMS_FLAT_URLS = False
CMS_REDIRECTS = True
CMS_SEO_FIELDS = True
CMS_MENU_TITLE_OVERWRITE = True
CMS_PERMISSION = True

CMS_SHOW_START_DATE = True
CMS_SHOW_END_DATE = True

# PLUGIN SETTINGS
IMAGE_ASPECT_RATIO_CHOICES = (
    (1, '1:1'),
    (1.33333, '4:3'),
    (1.77777, '16:9'),
    (2.33333, '21:9'),
)

# PLUGIN TEASER SETTINGS
CMSPLUGIN_FILER_TEASER_STYLE_CHOICES = [
    # ('plugin_teaser_picleft','Bild Links'),
]

# PLUGIN VIDEO SETTINGS
VIDEO_PLUGIN_ENABLE_ADVANCED_SETTINGS = False  # disable color settings etc

# compressor
COMPRESS_PARSER = 'compressor.parser.HtmlParser'
COMPRESS_OFFLINE = True
COMPRESS_OUTPUT_DIR = ''

# ckeditor text plugin
CKEDITOR_SETTINGS = {
    'height': 300,
    'stylesSet': 'default:/static/js/modules/ckeditor.wysiwyg.js',
    'contentsCss': ['/static/css/base.css'],
    'language': '{{ language }}',
    'toolbar': 'CMS',
    'skin': 'moono',
    'extraPlugins': 'cmsplugins',
}

# django admin shortcuts
ADMIN_SHORTCUTS = [
    {
        'shortcuts': [
            {
                'url': '/',
                'open_new_window': True,
            },
            {
                'url_name': 'admin:cms_page_changelist',
                'title': _('Pages'),
            },
            {
                'url_name': 'admin:filer_folder_changelist',
                'title': _('Files'),
            },
        ],
    }
]
