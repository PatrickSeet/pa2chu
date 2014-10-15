from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pa2chu.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'chu2pa.views.home', name='home'),
    url(r'^student_check/$', 'chu2pa.views.student_check', name='student_check'),
    url(r'^teacher/$', 'chu2pa.views.teacher', name='teacher'),
    url(r'^student/$', 'chu2pa.views.student', name='student'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^profile/$', 'chu2pa.views.profile', name='profile'),
    url(r'^faq/$', 'chu2pa.views.faq', name='faq'),
    url(r'^register/$', 'chu2pa.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),

)