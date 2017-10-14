from django.conf.urls import url, include

from account.forms import LoginUsernameForm, SignupForm, ChangePasswordForm, SettingsForm, PasswordResetForm, PasswordResetTokenForm

from .base import ViewConfig


label = "dua"
title = "Django User Accounts"
views = [
    ViewConfig(pattern=r"^account/signup/$", template="account/signup.html", name="account_signup", pattern_kwargs={}, form=SignupForm()),
    ViewConfig(pattern=r"^account/login/$", template="account/login.html", name="account_login", pattern_kwargs={}, form=LoginUsernameForm(), ACCOUNT_OPEN_SIGNUP=True),
    ViewConfig(pattern=r"^account/logout/$", template="account/logout.html", name="account_logout", pattern_kwargs={}),
    ViewConfig(pattern=r"^account/confirm_email/(?P<key>\w+)/$", template="account/email_confirm.html", name="account_confirm_email", pattern_kwargs={"key": "abc"}, confirmation={"key": "foo", "email_address": {"email": "example@sample.com"}}),
    ViewConfig(pattern=r"^account/password/$", template="account/password_change.html", name="account_password", pattern_kwargs={}, form=ChangePasswordForm(user=None)),
    ViewConfig(pattern=r"^account/password/reset/$", template="account/password_reset.html", name="account_password_reset", pattern_kwargs={}, form=PasswordResetForm()),
    ViewConfig(pattern=r"^account/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$", template="account/password_reset_token.html", name="account_password_reset_token", pattern_kwargs={"uidb36": "aaa", "token": "123"}, form=PasswordResetTokenForm()),
    ViewConfig(pattern=r"^account/settings/$", template="account/settings.html", name="account_settings", pattern_kwargs={}, form=SettingsForm()),
    ViewConfig(pattern=r"^account/delete/$", template="account/delete.html", name="account_delete", pattern_kwargs={}),
]
urlpatterns = [
    view.url()
    for view in views
]
url = url("", include("pinax_theme_tester.configs.dua"))
