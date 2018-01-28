from django.conf.urls import include, url
from django.urls import reverse
from pinax.invitations.forms import InviteForm
from pinax.invitations.models import JoinInvitation

from .base import ViewConfig


class User:
    @property
    def invitationstat(self):
        class CanSend:
            def can_send(self):
                return True
        return CanSend()


class Invite(dict):

    def __getattr__(self, attr):
        return getattr(JoinInvitation, attr)

    @property
    def status(self):
        return self["status"]


context = dict(
    can_send_user=User(),
    invites=[
        Invite(status=JoinInvitation.STATUS_SENT, to_user=dict(get_profile=dict(get_absolute_url="foo")), signup_code=dict(email="foo@example.com")),
        Invite(status=JoinInvitation.STATUS_ACCEPTED, signup_code=dict(email="bar@example.com")),
        Invite(status=JoinInvitation.STATUS_JOINED_INDEPENDENTLY, signup_code=dict(email="foobar@example.com")),
    ],
    total_invites_remaining=10,
    form=InviteForm(user=None)
)

patch = "http://pinaxproject.com/pinax-design/patches/pinax-invitations.svg"
label = "invitations"
title = "Pinax Invitations"
url_namespace = app_name = "pinax_invitations"

class NamespacedViewConfig(ViewConfig):

    def resolved_path(self):
        return reverse("{}:{}".format(url_namespace, self.name), kwargs=self.pattern_kwargs)

views = [
    NamespacedViewConfig(
        pattern=r"^fragments/$",
        template="fragments_invitations.html",
        template_source=[
            "pinax/invitations/_invite_form.html",
            "pinax/invitations/_invited.html",
            "pinax/invitations/_invites_remaining.html",
        ],
        name="invitations_fragments",
        pattern_kwargs={},
        **context),

    # Fake urls to handle template {% url %} needs
    NamespacedViewConfig(pattern=r"", template="", name="invite", pattern_kwargs={}, menu=False)
]
urlpatterns = [
    view.url()
    for view in views
]
url = url("invitations/", include("pinax_theme_tester.configs.invitations"))
