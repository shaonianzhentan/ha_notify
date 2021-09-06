from .shaonianzhentan import fetch_post

class WeWork:

    def __init__(self, hass, corpid, agentid, secret, touser):
        self.hass = hass
        self.corpid = corpid
        self.secret = secret
        self.agentid = agentid
        self.touser = touser
        self.token_expire_time = 0
        self.access_token = ""

    def send_message(data):
        print(data)