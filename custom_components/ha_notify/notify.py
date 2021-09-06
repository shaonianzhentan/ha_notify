import logging
import time
import datetime
import requests
import json
import os
import voluptuous as vol
import sys

from homeassistant.components.notify import (
    ATTR_MESSAGE,
    ATTR_TITLE,
    ATTR_DATA,
    ATTR_TARGET,
    PLATFORM_SCHEMA,
    BaseNotificationService,
)

_LOGGER = logging.getLogger(__name__)

from .qqmail import QQmail
from .wework import WeWork

def get_service(hass, config, discovery_info=None):
    return NotificationService(hass, config)

class NotificationService(BaseNotificationService):
    def __init__(self, hass, config):
        self.hass = hass
        # QQ邮箱配置
        qqmailConfig = config.get('qqmail')
        if qqmailConfig is not None:
            self.qqmail = QQmail(hass, qqmailConfig.get('qq'), qqmailConfig.get('code'))
        # 企业微信
        weworkConfig = config.get('wework')
        if weworkConfig is not None:
            self.wework = WeWork(hass, weworkConfig.get('corpid'), weworkConfig.get('agentid'), weworkConfig.get('secret'))

    async def async_send_message(self, message="", **kwargs):
        title = kwargs.get("title")
        data = kwargs.get("data") or {}
        # 邮箱
        if self.qqmail is not None:
            self.qqmail.send_message({
                'title': title,
                'message': message,
            })
        # 企业
        if self.wework is not None:
            self.wework.send_message({
                'title': title,
                'message': message,
            })