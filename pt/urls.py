from django.conf.urls import url

from .configs import dua
from .views import as_view


urlpatterns = [
    url(r"^$", as_view("homepage.html", dua=dua), name="home"),
]

urlpatterns.extend(dua.urls())
