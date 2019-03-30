from django.conf.urls import url, include
from django.urls import reverse

from .base import ViewConfig

import pinax.webanalytics.activity


context = dict(

)

patch = "http://pinaxproject.com/pinax-design/patches/pinax-webanalytics.svg"
label = "webanalytics"
title = "Pinax Webanalytics"
url_namespace = app_name = "pinax_webanalytics"

class NamespacedViewConfig(ViewConfig):

    def resolved_path(self):
        return reverse("{}:{}".format(url_namespace, self.name), kwargs=self.pattern_kwargs)

views = [
    NamespacedViewConfig(
        pattern=r"^fragments/$",
        template="fragments_webanalytics.html",
        template_source=[
            "pinax/webanalytics/_adwords_conversion.html",
            "pinax/webanalytics/_gauges.html",
            "pinax/webanalytics/_google.html",
            "pinax/webanalytics/_mixpanel.html",
        ],
        name="webanalytics_fragments",
        pattern_kwargs={},
        **context),
    # Fake urls to handle template {% url %} needs
    NamespacedViewConfig(pattern=r"", template="", name="ajax_list_signup", pattern_kwargs={}, menu=False),
]
urlpatterns = [
    view.url()
    for view in views
]
url = url("webanalytics/", include("pinax_theme_tester.configs.webanalytics"))