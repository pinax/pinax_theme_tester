from . import (
    dua,
    general,
    blog,
    announcements,
    cohorts,
    stripe,
    messages,
    likes,
    invitations,
    documents,
    notifications
)

CONFIG_MAP = {
    dua.label: dua,
    general.label: general,
    announcements.label: announcements,
    blog.label: blog,
    cohorts.label: cohorts,
    documents.label: documents,
    invitations.label: invitations,
    likes.label: likes,
    messages.label: messages,
    notifications.label: notifications,
    stripe.label: stripe,
}
