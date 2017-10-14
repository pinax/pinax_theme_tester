from datetime import datetime

from django.conf.urls import url, include
from django.urls import reverse

from pinax.messages.forms import MessageReplyForm

from .base import ViewConfig as BaseViewConfig

####  port back?
from django import forms
from django.contrib.auth import get_user_model
from pinax.messages.forms import UserModelChoiceField
from pinax.messages.hooks import hookset
from pinax.messages.models import Message


class NewMessageForm(forms.ModelForm):

    subject = forms.CharField()
    to_user = UserModelChoiceField(queryset=get_user_model().objects)  # @@@ had to remove .none
    content = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super(NewMessageForm, self).__init__(*args, **kwargs)
        self.fields["to_user"].queryset = hookset.get_user_choices(self.user)
        if self.initial.get("to_user") is not None:
            qs = self.fields["to_user"].queryset.filter(pk=self.initial["to_user"])
            self.fields["to_user"].queryset = qs

    def save(self, commit=True):
        data = self.cleaned_data
        return Message.new_message(
            self.user, [data["to_user"]], data["subject"], data["content"]
        )

    class Meta:
        model = Message
        fields = ['to_user', 'subject', 'content']
######


class FakeUser:
    id = 1


class Thread(dict):

    @property
    def userthread_set(self):
        class Filter:
            def filter(*args, **kwargs):
                return self["unread"]
        return Filter()

    @property
    def messages(self):
        class All:
            def all(*args):
                return self["message_list"]
        return All()


fake_user = FakeUser()
message = dict(
    sender=dict(username="phil", sent_at=datetime(2017, 10, 1, 9, 37)),
    content="Anim labore doner shank fatback ham enim burgdoggen ipsum pork chop deserunt.  Pancetta venison sausage officia sint.  Tri-tip hamburger pork chop dolor andouille.  Flank pork loin beef ribs, spare ribs bresaola dolore picanha tongue incididunt ham bacon."
)
thread = Thread(
    pk=1,
    get_absolute_url="/messages/threads/1/",
    users=dict(all=["bob", "sue", "larry"]),
    subject="This is a test message",
    latest_message=message,
    message_list=[
        message
    ],
    unread=True
)
thread_read = Thread(
    pk=1,
    get_absolute_url="/messages/threads/1/",
    users=dict(all=["sue", "larry"]),
    subject="Some other message",
    latest_message=message,
    message_list=[
        message
    ],
    unread=False
)
messages = [
    thread,
    thread_read
]
label = "messages"
title = "Pinax Messages"
url_namespace = "pinax_messages"


class ViewConfig(BaseViewConfig):

    def resolved_path(self):
        return reverse("{}:{}".format(url_namespace, self.name), kwargs=self.pattern_kwargs)


views = [
    ViewConfig(pattern=r"^inbox-empty/$", template="pinax/messages/inbox.html", name="inbox_empty", pattern_kwargs={}, threads=[]),
    ViewConfig(pattern=r"^inbox/$", template="pinax/messages/inbox.html", name="inbox", pattern_kwargs={}, threads=messages),
    ViewConfig(pattern=r"^create/$", template="pinax/messages/message_create.html", name="message_create", pattern_kwargs={}, form=NewMessageForm(user=fake_user)),
    ViewConfig(pattern=r"^threads/(?P<pk>\d+)/delete/$", template="pinax/messages/thread_confirm_delete.html", name="thread_delete", pattern_kwargs={"pk": 1}, thread=thread),
    ViewConfig(pattern=r"^threads/(?P<pk>\d+)/$", template="pinax/messages/thread_detail.html", name="thread_detail", pattern_kwargs={"pk": 1}, thread=thread, form=MessageReplyForm(thread=None, user=None)),
]
urlpatterns = [
    view.url()
    for view in views
]
url = url(r"messages/", include("pinax_theme_tester.configs.messages", namespace=url_namespace))
