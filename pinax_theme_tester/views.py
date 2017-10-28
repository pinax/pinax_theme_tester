from django.template.loader import get_template
from django.views.generic import TemplateView

from pygments import highlight
from pygments.lexers import DjangoLexer
from pygments.formatters import HtmlFormatter


class TemplateWithContextView(TemplateView):
    context = None
    config = None

    def get_template_names(self):
        if self.request.GET.get("source"):
            return "source.html"
        return super().get_template_names()

    def get_context_data(self, *args, **kwargs):
        ctx = super(TemplateWithContextView, self).get_context_data(*args, **kwargs)
        if self.template_name:
            template = get_template(self.template_name)
            source = highlight(template.template.source, DjangoLexer(), HtmlFormatter())
            ctx.update({"template_source": source, "template_name": self.template_name})
        if self.context is not None:
            ctx.update(self.context)
        return ctx


def as_view(template, config, **kwargs):
    return TemplateWithContextView.as_view(template_name=template, config=config, context=kwargs)
