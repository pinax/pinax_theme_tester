from django.views.generic import TemplateView


class TemplateWithContextView(TemplateView):
    context = None

    def get_context_data(self, *args, **kwargs):
        ctx = super(TemplateWithContextView, self).get_context_data(*args, **kwargs)
        if self.context is not None:
            ctx.update(self.context)
        return ctx
