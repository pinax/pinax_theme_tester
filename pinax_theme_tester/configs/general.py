from django.conf.urls import url, include

from .base import ViewConfig


label = "general"
title = "General"
views = [
    ViewConfig(pattern=r"^general/404/$", template="404.html", name="general_400", pattern_kwargs={}),
    ViewConfig(pattern=r"^general/500/$", template="500.html", name="general_500", pattern_kwargs={}),
    ViewConfig(pattern=r"^general/fragments/$", template="fragments.html", name="general_fragments", pattern_kwargs={}),
]
urlpatterns = [
    view.url()
    for view in views
]
url = url("", include("pinax_theme_tester.configs.general"))
