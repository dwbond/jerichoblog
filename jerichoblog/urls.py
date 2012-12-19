from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jerichoblog.views.home', name='home'),
    # url(r'^jerichoblog/', include('jerichoblog.foo.urls')),

    (r'^$', 'blog.views.index'),
    #homepage

    url(r'^post/(?P<slug>[^\.]+)', 'blog.views.view_post', name = 'view_blog_post'),

    url(r'^category/(?P<slug>[^\.]+)', 'blog.views.view_category', name ='view_blog_category'),

    url(r'^comments/', include('django.contrib.comments.urls')),

    url(r'^archive/(\d+)/(\d+)/$', 'blog.views.month', name = 'view_blog_archive'),

    url(r^'category-list/', 'blog.views.category_archive', name = 'view_category_list'),

    url(r^'history/', 'blog.views.month_archive', name = 'view_history'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
