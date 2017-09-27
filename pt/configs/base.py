from django.urls import reverse
from django.conf.urls import url

from pt.views import as_view


class ViewConfig(object):

    def __init__(self, name, pattern, template, pattern_kwargs, **kwargs):
        self.name = name
        self.pattern = pattern
        self.template = template
        self.context = kwargs
        self.pattern_kwargs = pattern_kwargs

    def make_view(self):
        return as_view(self.template, **self.context)

    def url(self):
        return url(self.pattern, self.make_view(), name=self.name)

    def resolved_path(self):
        return reverse(self.name, kwargs=self.pattern_kwargs)
