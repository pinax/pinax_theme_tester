from django.conf.urls import url, include

from django.contrib import messages
from django.contrib.messages.storage.base import Message
from .base import ViewConfig

messages = [
    Message(level=messages.DEBUG, message="This is a debug message"),
    Message(level=messages.INFO, message="This is a info message"),
    Message(level=messages.SUCCESS, message="This is a success message"),
    Message(level=messages.WARNING, message="This is a warning message"),
    Message(level=messages.ERROR, message="This is a error message"),
    Message(level=messages.ERROR, message="This is a error message with extra tags", extra_tags="extra-tag"),
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

patch = "http://pinaxproject.com/pinax-design/patches/blank.svg"
label = "general"
title = "General"
views = [
    ViewConfig(pattern=r"^general/404/$", template="404.html", name="general_400", pattern_kwargs={}),
    ViewConfig(pattern=r"^general/500/$", template="500.html", name="general_500", pattern_kwargs={}),
    ViewConfig(pattern=r"^general/fragments/$", template="fragments.html", name="general_fragments", pattern_kwargs={}, messages=messages, is_paginated=True, page_obj=page_obj, paginator=paginator),
]
urlpatterns = [
    view.url()
    for view in views
]
url = url("", include("pinax_theme_tester.configs.general"))
