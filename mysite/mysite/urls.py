from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from blog.sitemaps import PostSitemap  # исправлено: blog.sitemaps
from django.views.generic import RedirectView

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path(
        'sitemap.xml',
        sitemap,
        {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'
    ),
    path('', RedirectView.as_view(url='/blog/', permanent=True)),
]