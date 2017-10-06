from django.conf.urls import url

from .configs import CONFIG_MAP
from .views import as_view, set_template_set


urlpatterns = [
    url(r"^$", as_view("homepage.html"), name="home"),
    url(r"^__set_tmpl/$", set_template_set, name="set_template_set")
]

for label in CONFIG_MAP:
    urlpatterns.append(CONFIG_MAP[label].url)
