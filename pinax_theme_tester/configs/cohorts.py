from django.conf.urls import url, include
from django.urls import reverse
from django.utils import timezone

from pinax.cohorts.forms import CohortCreateForm
from account.hooks import hookset

from .base import ViewConfig as BaseViewConfig

cohort = {
    "pk": 1,
    "name": "Bacon Ipsum Dolor",
    "created": timezone.now(),
    "members": [
        dict(email="foo@bar.com"),
        dict(email="foo@bar.com", user="username"),
        dict(email="foo@bar.com", user="username"),
        dict(email="foo@bar.com", invited=True, signup_code=dict(code=hookset.generate_signup_code_token(email="foo@bar.com"), expiry=timezone.now(), sent=timezone.now(), created=timezone.now())),
        dict(email="foo@bar.com"),
        dict(email="foo@bar.com"),
        dict(email="foo@bar.com", invited=True, signup_code=dict(code=hookset.generate_signup_code_token(email="foo@bar.com"), expiry=timezone.now(), sent=timezone.now(), created=timezone.now())),
        dict(email="foo@bar.com", user="username"),
        dict(email="foo@bar.com")
    ],
    "member_counts": dict(users=3, total=9, pending=6)
}
cohort_list = [
    cohort,
    cohort,
    cohort,
    cohort
]
waiting_list = [
    dict(email="foo@bar.com", created=timezone.now(), pk=1),
    dict(email="foo@bar.com", created=timezone.now(), pk=1),
    dict(email="foo@bar.com", created=timezone.now(), pk=1),
    dict(email="foo@bar.com", created=timezone.now(), pk=1),
    dict(email="foo@bar.com", created=timezone.now(), pk=1),
    dict(email="foo@bar.com", created=timezone.now(), pk=1),
    dict(email="foo@bar.com", created=timezone.now(), pk=1),
    dict(email="foo@bar.com", created=timezone.now(), pk=1)
]


patch = "http://pinaxproject.com/pinax-design/patches/pinax-cohorts.svg"
label = "cohort"
title = "Pinax Cohorts"
url_namespace = "pinax_cohorts"
app_name = "pinax_cohorts"

class ViewConfig(BaseViewConfig):

    def resolved_path(self):
        return reverse("{}:{}".format(url_namespace, self.name), kwargs=self.pattern_kwargs)


views = [
    ViewConfig(pattern=r"^pinax-cohorts/$", template="pinax/cohorts/cohort_list.html", name="list", pattern_kwargs={}, cohorts=cohort_list),
    ViewConfig(pattern=r"^pinax-cohorts/create/$", template="pinax/cohorts/cohort_create.html", name="create", pattern_kwargs={}, form=CohortCreateForm()),
    ViewConfig(pattern=r"^pinax-cohorts/(?P<pk>\d+)/$", template="pinax/cohorts/cohort_detail.html", name="detail", pattern_kwargs={"pk": 1}, cohort=cohort, waiting_list=waiting_list),
    ViewConfig(pattern=r"^pinax-cohorts/(?P<pk>\d+)/add_member/$", template=None, name="member_add", pattern_kwargs={"pk": 1}, menu=False),
    ViewConfig(pattern=r"^pinax-cohorts/(?P<pk>\d+)/send_invitiations/$", template=None, name="send_invitations", pattern_kwargs={"pk": 1}, menu=False)
]
urlpatterns = [
    view.url()
    for view in views
]
url = url(r"", include("pinax_theme_tester.configs.cohorts", namespace=url_namespace))
