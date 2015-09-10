"""google_scholar_dual_cite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'google_scholar_dual_cite.core.views.home', name='home'),
    url(r'^api/papers', 'google_scholar_dual_cite.core.views.papers_by_query_api',
        name='papers_by_query_api'),
    url(r'^api/cites', 'google_scholar_dual_cite.core.views.cites_api',
        name='cites_api'),
]
