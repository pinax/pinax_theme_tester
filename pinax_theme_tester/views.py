from django.template.loader import get_template
from django.views.generic import TemplateView

from pygments import highlight
from pygments.lexers import DjangoLexer
from pygments.formatters import HtmlFormatter


class TemplateWithContextView(TemplateView):
    context = None
    config = None
    usage_name = None

    def get_template_names(self):
        if self.request.GET.get("source"):
            return "source.html"
        return super().get_template_names()

    def get_context_data(self, *args, **kwargs):
        ctx = super(TemplateWithContextView, self).get_context_data(*args, **kwargs)

        if self.config and self.config.template_source:
            # Explicit template source(s) takes priority
            if isinstance(self.config.template_source, str):
                # single template source file path
                template_sources = [self.config.template_source]
                if self.template_name and self.template_name != self.config.template_source:
                    self.usage_name = self.template_name
            else:
                # expecting an iterable of template source file paths
                template_sources = self.config.template_source
                self.usage_name = self.template_name
        elif self.template_name:
            # Default template
            template_sources = [self.template_name]

        templates = []
        for source in template_sources:
            # Add dictionary with name and source
            template = get_template(source)
            template_source = highlight(template.template.source, DjangoLexer(), HtmlFormatter())
            templates.append(dict(name=source, source=template_source))
        ctx.update({"templates": templates})

        # Display snippet usage
        if self.usage_name:
            usage = get_template(self.usage_name)
            usage_source = highlight(usage.template.source, DjangoLexer(), HtmlFormatter())
            ctx.update({"usage_source": usage_source})

        if self.context is not None:
            ctx.update(self.context)
        return ctx


def as_view(template, config, **kwargs):
    return TemplateWithContextView.as_view(template_name=template, config=config, context=kwargs)
