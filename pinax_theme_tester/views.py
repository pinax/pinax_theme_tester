from django.shortcuts import redirect
from django.views.decorators.http import require_POST

from django.views.generic import TemplateView


class TemplateWithContextView(TemplateView):
    context = None

    def get_context_data(self, *args, **kwargs):
        ctx = super(TemplateWithContextView, self).get_context_data(*args, **kwargs)
        if self.context is not None:
            ctx.update(self.context)
        return ctx


def as_view(template, **kwargs):
    return TemplateWithContextView.as_view(template_name=template, context=kwargs)


@require_POST
def set_template_set(request):
    from .configs import CONFIG_MAP  # ugly, I know, but whatever
    request.session["template_set"] = request.POST.get("template_set", None)
    config = CONFIG_MAP.get(request.session["template_set"])
    if config:
        return redirect([v for v in config.views if v.menu][0].resolved_path())
    return redirect("home")
