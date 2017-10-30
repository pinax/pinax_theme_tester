from django.conf import settings

from .configs import CONFIG_MAP


def template_set(request):
    context = {
        "available_configs": CONFIG_MAP,
        "pinax_notifications_installed": "pinax.notifications" in settings.INSTALLED_APPS,
        "pinax_stripe_installed": "pinax.stripe" in settings.INSTALLED_APPS
    }
    return context
