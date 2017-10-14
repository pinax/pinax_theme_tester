from django.conf.urls import url, include
from django.urls import reverse
from django.utils import timezone

from .base import ViewConfig as BaseViewConfig


post = {
    "title": "My Blog Post",
    "get_absolute_url": "/pinax-blog/post/1/",
    "teaser_html": "<p>Bacon ipsum dolor amet corned beef beef tri-tip venison, tongue shoulder meatball. Ribeye tail meatloaf brisket, short ribs porchetta short loin turkey. Cow leberkas capicola ham venison bresaola.</p>",
    "published": timezone.now(),
    "author": {
        "get_full_name": "Patrick Altman"
    },
    "section": {
        "slug": "all",
        "name": "All"
    },
    "description": "Bacon ipsum dolor amet corned beef beef tri-tip venison",
    "content_html": """<h2>Ham Enim Burgdoggen</h2><p>Spicy jalapeno bacon ipsum dolor amet sint tri-tip pork loin shoulder kevin.  T-bone pork chop in hamburger non leberkas.  Ipsum capicola est t-bone nostrud officia tail.  Burgdoggen sint duis, bacon reprehenderit incididunt exercitation cupim lorem picanha labore venison sirloin.  Biltong rump ribeye voluptate ad.</p>
<p>Anim labore doner shank fatback ham enim burgdoggen ipsum pork chop deserunt.  Pancetta venison sausage officia sint.  Tri-tip hamburger pork chop dolor andouille.  Flank pork loin beef ribs, spare ribs bresaola dolore picanha tongue incididunt ham bacon.  T-bone esse chuck pariatur magna labore.  Fugiat t-bone pork chop ball tip.  Cow pork belly incididunt lorem swine rump ham ut voluptate.</p>
<p>Tempor cow short ribs, <strong>chicken pork belly</strong> pastrami brisket dolore.  Occaecat shank cow aute qui.  Eu flank dolor strip steak consequat occaecat aliqua tongue tenderloin pariatur.  Shank filet mignon incididunt sint brisket, et turkey.  Frankfurter veniam incididunt pastrami ham cupim in.  Sausage hamburger ribeye tri-tip minim cillum, pancetta turkey andouille nisi.</p>
<blockquote>Tempor cow short ribs, chicken pork belly pastrami brisket dolore.</blockquote>
<h3>Minim non picanha do ipsum.</h3>
<p>Burgdoggen biltong boudin strip steak.  Meatloaf jerky est velit in pastrami labore t-bone aute ut bacon prosciutto beef quis anim.  Non doner kielbasa dolore.  Porchetta landjaeger mollit rump deserunt kevin corned beef ribeye.</p>
<p>Nulla cow proident alcatra kevin capicola filet mignon cillum tongue venison, veniam sausage t-bone ullamco tail.  Andouille laborum turkey jerky.  Tail doner biltong andouille, ullamco corned beef cow fugiat rump incididunt magna ribeye.  Anim pork loin spare ribs kielbasa.  Turducken sed shank bresaola ham meatloaf.</p>
    """

}
post_list = [
    post,
    post,
    post,
    post
]
page_obj = {
    "has_previous": True,
    "has_next": False,
    "previous_page_number": 1,
    "next_page_number": 10,
    "number": 5
}
paginator = {
    "page_range": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
}

label = "blog"
title = "Pinax Blog"
url_namespace = "pinax_blog"


class ViewConfig(BaseViewConfig):

    def resolved_path(self):
        return reverse("{}:{}".format(url_namespace, self.name), kwargs=self.pattern_kwargs)


views = [
    ViewConfig(pattern=r"^feed/(?P<section>[-\w]+)/(?P<feed_type>[-\w]+)/$", template="pinax/blog/blog_list.html", name="blog_feed", pattern_kwargs={}, menu=False),
    ViewConfig(pattern=r"^pinax-blog/list/$", template="pinax/blog/blog_list.html", name="blog", pattern_kwargs={}, current_section="all", post_list=post_list, section="all", feed_type="atom", is_paginated=True, page_obj=page_obj, paginator=paginator),
    ViewConfig(pattern=r"^pinax-blog/list-empty/$", template="pinax/blog/blog_list.html", name="blog_empty", pattern_kwargs={}, current_section="all", post_list=None),
    ViewConfig(pattern=r"^pinax-blog/section/(?P<section>[-\w]+)/$", template="pinax/blog/blog_list.html", name="blog_section", pattern_kwargs={"section": "all"}, post_list=post_list, menu=False),
    ViewConfig(pattern=r"^pinax-blog/post/(?P<post_pk>\d)/$", template="pinax/blog/blog_post.html", name="blog_post_pk", pattern_kwargs={"post_pk": 1}, post=post)
]
urlpatterns = [
    view.url()
    for view in views
]
url = url(r"", include("pinax_theme_tester.configs.blog", namespace=url_namespace))
