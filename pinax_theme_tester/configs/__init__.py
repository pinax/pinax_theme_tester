from . import (
    dua,
    general,
    announcements,
    blog,
    cohorts,
    documents,
    invitations,
    likes,
    messages,
    notifications,
    stripe,
    waitinglist,
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
    waitinglist.label: waitinglist,
}
