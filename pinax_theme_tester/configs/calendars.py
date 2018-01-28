from collections import defaultdict
import datetime

from django.conf.urls import include, url
from django.utils import timezone

from pinax.calendars.adapters import EventAdapter

from .base import ViewConfig


class FakeEventAdapter(EventAdapter):
    day_url_name = "daily"
    month_url_name = "monthly"

    def events_by_day(self, year, month, tz, **kwargs):
        days = defaultdict(list)
        for event in self.events:
            if event[1].month == month:
                days[event[1].day].append(event[0])
        return days

timestamp = timezone.now()
today = timestamp.date()
yesterday = (timestamp - datetime.timedelta(days=1)).date()
tomorrow = (timestamp + datetime.timedelta(days=1)).date()

events = (
    ("Yesterday's Event", yesterday),
    ("Today's Big Event", today),
    ("Tomorrow's Event", tomorrow),
)

context = dict(
    the_date=today,
    events=FakeEventAdapter(events)
)

patch = "http://pinaxproject.com/pinax-design/patches/pinax-calendars.svg"
label = "calendars"
title = "Pinax Calendars"

views = [
    ViewConfig(
        pattern=r"^templatetags/$",
        template="templatetags_calendars.html",
        template_source="pinax/calendars/calendar.html",
        name="calendars_templatetags",
        pattern_kwargs={},
        **context),
    # Fake urls to handle adapter reverse() calls
    ViewConfig(pattern="(?P<year>\d+)/(?P<month>\d+)/", template="", name="monthly", pattern_kwargs={}, menu=False),
    ViewConfig(pattern="(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/", template="", name="daily", pattern_kwargs={}, menu=False),
]
urlpatterns = [
    view.url()
    for view in views
]
url = url(r"calendars/", include("pinax_theme_tester.configs.calendars"))
