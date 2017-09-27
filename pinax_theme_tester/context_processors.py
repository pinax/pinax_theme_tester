from .configs import CONFIG_MAP


def template_set(request):
    tset = request.session.get("template_set", None)
    context = {
        "current_config": None,
        "available_configs": CONFIG_MAP
    }
    if tset:
        context["current_config"] = CONFIG_MAP.get(tset)
    return context
