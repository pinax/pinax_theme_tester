from django.conf.urls import url, include
from django.urls import reverse

from .base import ViewConfig

from pinax.waitinglist.forms import WaitingListEntryForm


context = dict(
    form=WaitingListEntryForm()
)

patch = "http://pinaxproject.com/pinax-design/patches/pinax-waitinglist.svg"
label = "waitinglist"
title = "Pinax Waitinglist"
url_namespace = app_name = "pinax_waitinglist"

class NamespacedViewConfig(ViewConfig):

    def resolved_path(self):
        return reverse("{}:{}".format(url_namespace, self.name), kwargs=self.pattern_kwargs)

views = [
    NamespacedViewConfig(pattern=r"^fragments/$", template="fragments_waitinglist.html", name="waitinglist_fragments", pattern_kwargs={}, **context),
    # Fake urls to handle template {% url %} needs
    NamespacedViewConfig(pattern=r"", template="", name="ajax_list_signup", pattern_kwargs={}, menu=False),
]
urlpatterns = [
    view.url()
    for view in views
]
url = url("waitinglist/", include("pinax_theme_tester.configs.waitinglist"))
