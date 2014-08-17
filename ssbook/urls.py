from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ssbook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns ('',
	(r'^book/', include('book.urls')),
)

urlpatterns += staticfiles_urlpatterns()
#urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

