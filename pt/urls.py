from django.conf.urls import url

from .views import TemplateWithContextView


def as_view(template, context):
    return TemplateWithContextView.as_view(template_name=template, context=context)


urlpatterns = [
    url(r"^$", as_view("homepage.html", {"foo": "Bar"}), name="home"),
]
