from datetime import datetime

from django.conf.urls import url, include
from django.contrib.auth.models import User
from django.urls import reverse

from pinax.documents.forms import FolderCreateForm, DocumentCreateForm, FolderShareForm
from pinax.documents.models import Folder

from .base import ViewConfig as BaseViewConfig
from .base import dotdict


class Member(dotdict):
    def can_share(self, user):
        return True


class ShareForm(FolderShareForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["participants"].queryset = User.objects.all()


storage = dotdict(bytes_used=62345253, bytes_total=100522999, color="danger", percentage="62")
user = dotdict(first_name="Patrick", last_name="Altman")
folder = Member(id=1, name="My Folder", icon="folder-open", size=35235266, modified=datetime(2017, 10, 1, 13, 21), modified_by=user, shared_ui=False, get_absolute_url="/documents/f/1/")
member = Member(id=1, name="My Document.txt", icon="file", get_absolute_url="/foo/", size=373737, modified=datetime(2017, 10, 1, 13, 21), shared_ui=True, modified_by=user, download_url="/foo/download/", delete_url="/foo/delete/")


patch = "http://pinaxproject.com/pinax-design/patches/pinax-documents.svg"
label = "documents"
title = "Pinax Documents"
url_namespace = "pinax_documents"
app_name = "pinax_documents"

class ViewConfig(BaseViewConfig):
    def resolved_path(self):
        return reverse("{}:{}".format(url_namespace, self.name), kwargs=self.pattern_kwargs)


views = [
    ViewConfig(pattern=r"^$", template="pinax/documents/index.html", name="document_index", pattern_kwargs={}, storage=storage, folder=folder, members=[member, folder]),
    ViewConfig(pattern=r"^d/create/$", template="pinax/documents/document_create.html", name="document_create", pattern_kwargs={}, form=DocumentCreateForm(folders=Folder.objects.all(), storage=storage), folder=folder),
    ViewConfig(pattern=r"^d/(?P<pk>\d+)/$", template="pinax/documents/document_detail.html", name="document_detail", pattern_kwargs={"pk": 1}, document=member),
    ViewConfig(pattern=r"^d/(?P<pk>\d+)/download/$", template="", name="document_download", pattern_kwargs={"pk": 1}, menu=False),
    ViewConfig(pattern=r"^d/(?P<pk>\d+)/delete/$", template="pinax/documents/document_confirm_delete.html", name="document_delete", pattern_kwargs={"pk": 1}, document=member),
    ViewConfig(pattern=r"^f/create/$", template="pinax/documents/folder_create.html", name="folder_create", pattern_kwargs={}, form=FolderCreateForm(folders=Folder.objects.all()), parent=folder),
    ViewConfig(pattern=r"^f/(?P<pk>\d+)/$", template="pinax/documents/folder_detail.html", name="folder_detail", pattern_kwargs={"pk": 1}, folder=folder, members=[member]),
    ViewConfig(pattern=r"^f/(?P<pk>\d+)/share/$", template="pinax/documents/folder_share.html", name="folder_share", pattern_kwargs={"pk": 1}, form=ShareForm(), folder=folder, participants=[dotdict(username="foo"), dotdict(username="bar")]),
    ViewConfig(pattern=r"^f/(?P<pk>\d+)/delete/$", template="pinax/documents/folder_confirm_delete.html", name="folder_delete", pattern_kwargs={"pk": 1}, folder=folder),
]
urlpatterns = [
    view.url()
    for view in views
]
url = url(r"^documents/", include("pinax_theme_tester.configs.documents", namespace=url_namespace))
