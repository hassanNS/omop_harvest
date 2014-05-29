import re
from django.conf.urls import url, patterns, include
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView
from django.template import add_to_builtins

add_to_builtins('avocado.templatetags.avocado_tags')

admin.autodiscover()

<<<<<<< HEAD
<<<<<<< HEAD
urlpatterns = patterns('',
    # Landing Page
    url(r'^$', 'omop_harvest.views.landing', name='landing'),

=======
urlpatterns = patterns(
    '',
    # Landing Page
    url(r'^$', 'omop_harvest.views.landing', name='landing'),
>>>>>>> 0e24556... Adding Containerization (Docker) and Subfolder for Continuous Integration and Deployment (CID)
=======
urlpatterns = patterns(
    '',
    # Landing Page
    url(r'^$', 'omop_harvest.views.landing', name='landing'),
>>>>>>> 1f16dee... Adding urls.py from ATI template
    # Cilantro Pages
    url(r'^workspace/', TemplateView.as_view(template_name='index.html'), name='workspace'),
    url(r'^query/', TemplateView.as_view(template_name='index.html'), name='query'),
    url(r'^results/', TemplateView.as_view(template_name='index.html'), name='results'),
<<<<<<< HEAD
<<<<<<< HEAD

    # Serrano-compatible Endpoint
    url(r'^api/', include('serrano.urls')),

=======
    # Serrano-compatible Endpoint
    url(r'^api/', include('serrano.urls')),
>>>>>>> 0e24556... Adding Containerization (Docker) and Subfolder for Continuous Integration and Deployment (CID)
    # Administrative components
    url(r'^admin/', include(admin.site.urls)),

    #CHOPAuth URLs
    url(r'^register/$', 'registration.views.register',{'template_name':'registration.html'},name='register'),
    url(r'^register/complete/$', TemplateView.as_view(template_name='registration_complete.html'),
        name='registration-complete'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name':'login.html'}, name='login'),
<<<<<<< HEAD
<<<<<<< HEAD
    
    url(r'^', include('chopauth.urls')),
)

=======
)

=======
)

>>>>>>> 1b088df... Make chopauth functional in dev/prod and optional in local
# If chopauth is available, include those urls
try:
    urlpatterns += patterns('',
        url(r'^', include('chopauth.urls')),
    )
except ImportError:
    urlpatterns += patterns('',
        url(r'^', include('registration.urls')),
    )

<<<<<<< HEAD
>>>>>>> 0e24556... Adding Containerization (Docker) and Subfolder for Continuous Integration and Deployment (CID)
=======
>>>>>>> 1b088df... Make chopauth functional in dev/prod and optional in local
=======
    # Serrano-compatible Endpoint
    url(r'^api/', include('serrano.urls')),
    # Administrative components
    url(r'^admin/', include(admin.site.urls)),

    #CHOPAuth URLs
    url(r'^register/$', 'registration.views.register',{'template_name':'registration.html'},name='register'),
    url(r'^register/complete/$', TemplateView.as_view(template_name='registration_complete.html'),
        name='registration-complete'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name':'login.html'}, name='login'),
)

<<<<<<< HEAD
>>>>>>> 1f16dee... Adding urls.py from ATI template
=======
# If chopauth is available, include those urls
try:
    urlpatterns += patterns('',
        url(r'^', include('chopauth.urls')),
    )
except ImportError:
    urlpatterns += patterns('',
        url(r'^', include('registration.urls')),
    )

>>>>>>> dfc280c... Adding in chop auth settings into urls.py
# In production, these two locations must be served up statically
urlpatterns += patterns('django.views.static',
    url(r'^{0}(?P<path>.*)$'.format(re.escape(settings.MEDIA_URL.lstrip('/'))), 'serve', {
        'document_root': settings.MEDIA_ROOT
    }),
    url(r'^{0}(?P<path>.*)$'.format(re.escape(settings.STATIC_URL.lstrip('/'))), 'serve', {
        'document_root': settings.STATIC_ROOT
    }),
)
