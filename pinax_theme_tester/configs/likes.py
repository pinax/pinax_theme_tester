from django.conf.urls import url, include

from .base import ViewConfig


class LikedObject:
    def get_absolute_url(self):
        return "/"

    def __str__(self):
        return "Fantastic Object"


context = dict(
    liked_object=LikedObject(),
    like=dict(type="foo"),
    instance="Fantastic Object",
    like_url="/like/url/",
    like_text="Liked",
    like_class="liked",
    like_count=37,
    counts_text="Fantastics"
)

patch = "http://pinaxproject.com/pinax-design/patches/pinax-likes.svg"
label = "likes"
title = "Pinax Likes"

views = [
    ViewConfig(pattern=r"^fragments/$", template="fragments_likes.html", name="likes_fragments", pattern_kwargs={}, **context),
]
urlpatterns = [
    view.url()
    for view in views
]
url = url("likes/", include("pinax_theme_tester.configs.likes"))
