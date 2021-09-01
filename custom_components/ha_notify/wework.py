
class WeWork:

    def __init__(self, hass, corpid, agentid, corpsecret, touser):
        self.hass = hass
        self.corpid = corpid
        self.corpsecret = corpsecret
        self.agentid = agentid
        self.touser = touser
        self.token_expire_time = 0
        self.access_token = ""