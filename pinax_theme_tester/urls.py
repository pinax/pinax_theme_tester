from django.conf.urls import url

from .configs import CONFIG_MAP
from .views import as_view


urlpatterns = [
    url(r"^$", as_view("homepage.html", config=None), name="home")
]

for label in CONFIG_MAP:
    urlpatterns.append(CONFIG_MAP[label].url)
