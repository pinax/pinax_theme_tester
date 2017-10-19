import copy

from django.conf.urls import url, include
from django.urls import reverse

from .base import ViewConfig as BaseViewConfig


context = dict(
    notice_settings=dict(
        column_headers=[
            dict(title="Email"),
            dict(title="SMS"),
            dict(title="On Site")
        ],
        rows=[
            dict(notice_type=dict(display="Friend Signs Up", description="Get notified when one of your social friends signs up on the site."), cells=[
                ("_foo", True),
                ("_foo", False),
                ("_foo", True)
            ]),
            dict(notice_type=dict(display="Friend Request", description="Get notified when someone requests your friendship."), cells=[
                ("_foo", False),
                ("_foo", True),
                ("_foo", True)
            ]),
            dict(notice_type=dict(display="Private Message", description="Get notified when you receive a private message"), cells=[
                ("_foo", False),
                ("_foo", False),
                ("_foo", False)
            ]),
            dict(notice_type=dict(display="Got Paid", description="Get notified when your friend pays you $1,000,000"), cells=[
                ("_foo", True),
                ("_foo", True),
                ("_foo", True)
            ])
        ]
    )
)
with_email_context = copy.deepcopy(context)
with_email_context.update(
    dict(request=dict(user=dict(email="foo@bar.com"))),
)


patch = "http://pinaxproject.com/pinax-design/patches/pinax-notifications.svg"
label = "notifications"
title = "Pinax Notifications"
url_namespace = "pinax_notifications"


class ViewConfig(BaseViewConfig):

    def resolved_path(self):
        return reverse("{}:{}".format(url_namespace, self.name), kwargs=self.pattern_kwargs)


views = [
    ViewConfig(pattern=r"^settings/$", template="pinax/notifications/notice_settings.html", name="notice_settings", pattern_kwargs={}, **with_email_context),
    ViewConfig(pattern=r"^settings/no-confirmed-email-state/$", template="pinax/notifications/notice_settings.html", name="notice_settings_no_confirmed_email", pattern_kwargs={}, **context)
]
urlpatterns = [
    view.url()
    for view in views
]
url = url(r"notifications/", include("pinax_theme_tester.configs.notifications", namespace=url_namespace))
