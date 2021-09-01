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

def get_service(hass, config, discovery_info=None):
    return NotificationService(hass, config)

class NotificationService(BaseNotificationService):
    def __init__(self, hass, config):
        self.hass = hass

    async def async_send_message(self, message="", **kwargs):
        title = kwargs.get("title")
        data = kwargs.get("data") or {}
        
        