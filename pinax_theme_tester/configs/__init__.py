from . import (
    dua,
    general,
    blog,
    announcements,
    cohorts,
    stripe,
    messages,
    likes,
    invitations
)

CONFIG_MAP = {
    dua.label: dua,
    general.label: general,
    blog.label: blog,
    announcements.label: announcements,
    cohorts.label: cohorts,
    stripe.label: stripe,
    messages.label: messages,
    likes.label: likes,
    invitations.label: invitations
}
