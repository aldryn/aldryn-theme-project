from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from cms.sitemaps import CMSSitemap

admin.autodiscover()

handler404 = "core.error_views.page_not_found"
handler500 = "core.error_views.server_error"

urlpatterns = patterns('',
    url(r'^static/(?P<path>.*)$', 'django.contrib.staticfiles.views.serve', {'insecure': True}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^', include('filer.server.urls')),
    url(r'^i18n/setlang/$', 'django.views.i18n.set_language'),
    url(r'^_ht/', include('health_check.urls')),
    # don't forget to add an "allow all" rule when going live!
    url(r'^robots\.txt$', include('robots.urls')),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': {'cmspages': CMSSitemap}}),
) + i18n_patterns('',
    url(r'^admin/login-as/', include('login_as.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # cms3 requirements
    url(r'^select2/', include('django_select2.urls')),

    # cms urls must be the last pattern!
    url(r'', include('cms.urls')),
)
