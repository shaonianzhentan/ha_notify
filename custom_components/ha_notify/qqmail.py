# ----------邮件相关---------- #
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

_LOGGER = logging.getLogger(__name__)

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
# ----------邮件相关---------- #

class QQmail:

    def __init__(self, hass, qq, code):
        self.hass = hass
        _qq = str(qq)
        if '@' not in _qq:
            _qq = _qq + '@qq.com'
        self.qq = _qq
        self.code = code

    # 发送邮件
    def sendMail(self, to_addr, _title, _message):
        try:
            from_addr = self.qq
            smtp_server = 'smtp.qq.com'
            msg = MIMEText(_message, 'html', 'utf-8')
            msg['From'] = _format_addr('HomeAssistant <%s>' % from_addr)
            #msg['To'] = _format_addr('智能家居 <%s>' % to_addr)
            msg['To'] = ','.join(to_addr)
            msg['Subject'] = Header(_title, 'utf-8').encode()
            server = smtplib.SMTP(smtp_server, 25)
            server.set_debuglevel(1)
            server.login(from_addr, self.code)
            server.sendmail(from_addr, to_addr, msg.as_string())
            server.quit()            
            _LOGGER.debug('【' + _title + '】邮件通知发送成功')
        except Exception as e:
            _LOGGER.debug('【' + _title + '】邮件通知发送失败')
            _LOGGER.debug(e)

    def send_message(data):
        print(data)