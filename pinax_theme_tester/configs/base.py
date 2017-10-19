from django.urls import reverse
from django.conf.urls import url

from pinax_theme_tester.views import as_view


class ViewConfig(object):

    def __init__(self, name, pattern, template, pattern_kwargs, menu=True, display_name=None, **kwargs):
        self.name = name
        self.pattern = pattern
        self.template = template
        self.context = kwargs
        self.pattern_kwargs = pattern_kwargs
        self.menu = menu
        self._display_name = display_name
        self.context.update(dict(current_view=self))

    def make_view(self):
        return as_view(self.template, **self.context)

    def url(self):
        return url(self.pattern, self.make_view(), name=self.name)

    def resolved_path(self):
        return reverse(self.name, kwargs=self.pattern_kwargs)

    def display_name(self):
        return self._display_name or self.name.replace("_", " ").title()

    def short_template_name(self):
        return self.template.split("/")[-1]


class dotdict(dict):
    """
    dot.notation access to dictionary attributes
    """
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
