from .configs import CONFIG_MAP


def template_set(request):
    context = {
        "available_configs": CONFIG_MAP
    }
    return context
