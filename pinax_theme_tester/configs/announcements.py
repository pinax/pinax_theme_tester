from django.conf.urls import url, include
from django.urls import reverse
from django.utils import timezone

from pinax.announcements.forms import AnnouncementForm

from .base import ViewConfig as BaseViewConfig


patch = "http://pinaxproject.com/pinax-design/patches/pinax-announcements.svg"
announcement = {
    "pk": 1,
    "title": "Bacon ipsum dolor amet corned beef beef tri-tip venison",
    "publish_start": timezone.now(),
    "publish_end": timezone.now(),
    "content": "Anim labore doner shank fatback ham enim burgdoggen ipsum pork chop deserunt.  Pancetta venison sausage officia sint.  Tri-tip hamburger pork chop dolor andouille.  Flank pork loin beef ribs, spare ribs bresaola dolore picanha tongue incididunt ham bacon."
}
announcement_list = [
    announcement,
    announcement,
    announcement,
    announcement
]

label = "announcement"
title = "Pinax Announcements"
url_namespace = "pinax_announcements"
app_name = "pinax_announcements"


class ViewConfig(BaseViewConfig):

    def resolved_path(self):
        return reverse("{}:{}".format(url_namespace, self.name), kwargs=self.pattern_kwargs)


views = [
    ViewConfig(pattern=r"^pinax-announcements/$", template="pinax/announcements/announcement_list.html", name="announcement_list", pattern_kwargs={}, announcement_list=announcement_list),
    ViewConfig(pattern=r"^pinax-announcements/create/$", template="pinax/announcements/announcement_form.html", name="announcement_create", pattern_kwargs={}, form=AnnouncementForm()),
    ViewConfig(pattern=r"^pinax-announcements/(?P<pk>\d+)/update/$", template="pinax/announcements/announcement_form.html", name="announcement_update", pattern_kwargs={"pk": 1}, form=AnnouncementForm(), announcement=announcement),
    ViewConfig(pattern=r"^pinax-announcements/(?P<pk>\d+)/$", template="pinax/announcements/announcement_detail.html", name="announcement_detail", pattern_kwargs={"pk": 1}, announcement=announcement),
    ViewConfig(pattern=r"^pinax-announcements/(?P<pk>\d+)/delete/$", template="pinax/announcements/announcement_confirm_delete.html", name="announcement_delete", pattern_kwargs={"pk": 1}, announcement=announcement),
    ViewConfig(pattern=r"^pinax-announcements/(?P<pk>\d+)/update/$", template="pinax/blog/blog_post.html", name="announcement_update", pattern_kwargs={"pk": 1}, menu=False),
    ViewConfig(pattern=r"^pinax-announcements/(?P<pk>\d+)/hide/$", template="pinax/blog/blog_post.html", name="announcement_dismiss", pattern_kwargs={"pk": 1}, menu=False)
]
urlpatterns = [
    view.url()
    for view in views
]
url = url(r"", include("pinax_theme_tester.configs.announcements", namespace=url_namespace))
