"""
sentry_bearychat.plugin
~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2015 by BearyInnovative Team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""
import sentry_bearychat

from django import forms

import logging

from sentry.plugins.bases import notify
from sentry.http import safe_urlopen
from sentry.utils.safe import safe_execute

class BearyChatOptionsForm(notify.NotificationConfigurationForm):
    webhook = forms.CharField(
        help_text='Your custom BearyChat webhook URL',
        widget=forms.TextInput(attrs={'class': 'span8'}))


class BearyChatPlugin(notify.NotificationPlugin):
    author = 'BearyInnovative Team'
    author_url = 'https://github.com/bearyinnovative'
    resource_links = [
        ('Bug Tracker', 'https://github.com/bearyinnovative/sentry-bearychat/issues'),
        ('Source', 'https://github.com/bearyinnovative/sentry-bearychat'),
    ]
    version = sentry_bearychat.VERSION
    title = 'BearyChat'
    slug = 'bearychat'
    description = "Post notifications to a BeayChat channel."
    conf_title = title
    conf_key = 'bearychat'
    project_conf_form = BearyChatOptionsForm
    logger = logging.getLogger('sentry.plugins.bearychat')

    # use same data structure as Webhook plugin
    def get_group_data(self, group, event):
        data = {
            'id': str(group.id),
            'project': group.project.slug,
            'project_name': group.project.name,
            'logger': group.logger,
            'level': group.get_level_display(),
            'culprit': group.culprit,
            'message': event.message,
            'url': group.get_absolute_url(),
        }
        data['event'] = dict(event.data or {})
        data['event']['tags'] = event.get_tags()
        return data

    def send_webhook(self, url, payload):
        return safe_urlopen(
            url=url,
            json=payload,
            timeout=3,
            verify_ssl=False,
        )

    def notify_users(self, group, event, fail_silently=False):
        payload = self.get_group_data(group, event)
        safe_execute(self.send_webhook, webhook, payload)
