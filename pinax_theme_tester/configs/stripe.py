import decimal
from datetime import datetime

from django.conf import settings
from django.conf.urls import url, include

from pinax.stripe.forms import PlanForm

from .base import ViewConfig

invoices = [
    dict(date=datetime(2017, 10, 1), subscription=dict(plan=dict(name="Pro")), period_start=datetime(2017, 10, 1), period_end=datetime(2017, 10, 31), total=decimal.Decimal("9.99"), paid=False),
    dict(date=datetime(2017, 9, 1), subscription=dict(plan=dict(name="Pro")), period_start=datetime(2017, 9, 1), period_end=datetime(2017, 9, 30), total=decimal.Decimal("9.99"), paid=True),
    dict(date=datetime(2017, 8, 1), subscription=dict(plan=dict(name="Beginner")), period_start=datetime(2017, 8, 1), period_end=datetime(2017, 8, 31), total=decimal.Decimal("5.99"), paid=True),
    dict(date=datetime(2017, 7, 1), subscription=dict(plan=dict(name="Beginner")), period_start=datetime(2017, 7, 1), period_end=datetime(2017, 7, 30), total=decimal.Decimal("5.99"), paid=True),
]
card = dict(pk=1, brand="Visa", last4="4242", exp_month="10", exp_year="2030", created_at=datetime(2016, 4, 5))
methods = [
    card
]
subscription = dict(pk=1, current_period_start=datetime(2017, 10, 1), current_period_end=datetime(2017, 10, 31), plan=dict(name="Pro"), start=datetime(2017, 10, 1), status="active", invoice_set=dict(all=invoices))
subscriptions = [
    subscription
]

patch = "http://pinaxproject.com/pinax-design/patches/pinax-stripe.svg"
label = "stripe"
title = "Pinax Stripe"

views = [
    ViewConfig(pattern=r"^invoices-empty/$", template="pinax/stripe/invoice_list.html", name="invoice_list_empty", pattern_kwargs={}, object_list=[]),
    ViewConfig(pattern=r"^invoices/$", template="pinax/stripe/invoice_list.html", name="pinax_stripe_invoice_list", pattern_kwargs={}, object_list=invoices),
    ViewConfig(pattern=r"^methods-empty/$", template="pinax/stripe/paymentmethod_list.html", name="method_list_empty", pattern_kwargs={}, object_list=[]),
    ViewConfig(pattern=r"^methods/$", template="pinax/stripe/paymentmethod_list.html", name="pinax_stripe_payment_method_list", pattern_kwargs={}, object_list=methods),
    ViewConfig(pattern=r"^methods/create/$", template="pinax/stripe/paymentmethod_create.html", name="pinax_stripe_payment_method_create", pattern_kwargs={}, PINAX_STRIPE_PUBLIC_KEY=settings.PINAX_STRIPE_PUBLIC_KEY),
    ViewConfig(pattern=r"^methods/update/(?P<pk>\d+)/$", template="pinax/stripe/paymentmethod_update.html", name="pinax_stripe_payment_method_update", pattern_kwargs={"pk": 1}, object=card),
    ViewConfig(pattern=r"^methods/delete/(?P<pk>\d+)/", template="pinax/stripe/paymentmethod_delete.html", name="pinax_stripe_payment_method_delete", pattern_kwargs={"pk": 1}, object=card),
    ViewConfig(pattern=r"^subscriptions-empty/$", template="pinax/stripe/subscription_list.html", name="subscription_list_empty", pattern_kwargs={}, object_list=[]),
    ViewConfig(pattern=r"^subscriptions/$", template="pinax/stripe/subscription_list.html", name="pinax_stripe_subscription_list", pattern_kwargs={}, object_list=subscriptions),
    ViewConfig(pattern=r"^subscriptions/create/$", template="pinax/stripe/subscription_create.html", name="pinax_stripe_subscription_create", pattern_kwargs={}, form=PlanForm(), request=dict(user=dict(customer=dict(default_source="foo")))),
    ViewConfig(pattern=r"^subscriptions/update/(?P<pk>\d+)/$", template="pinax/stripe/subscription_update.html", name="pinax_stripe_subscription_update", pattern_kwargs={"pk": 1}, object=subscription, form=PlanForm(), PINAX_STRIPE_PUBLIC_KEY=settings.PINAX_STRIPE_PUBLIC_KEY),
    ViewConfig(pattern=r"^subscriptions/delete/(?P<pk>\d+)/", template="pinax/stripe/subscription_delete.html", name="pinax_stripe_subscription_delete", pattern_kwargs={"pk": 1}, object=subscription),
]
urlpatterns = [
    view.url()
    for view in views
]
url = url(r"payments/", include("pinax_theme_tester.configs.stripe"))
