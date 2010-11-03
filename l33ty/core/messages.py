import time
import settings

class Request(object):

    def __init__(self, message, user, channel):
        self.length = len(message)
        message = unicode(message)

        message = self.remove_greeting_from_message(message)
        self.msg = message
        self.msg = self.msg.strip()
        self.user, _, self.host = user.partition('!')
        self.channel = channel

        self.time = time.time()

    def remove_greeting_from_message(self, msg):
        msg = msg.lstrip(getattr(settings, 'ACTIVATION_PREFIX', '|')).strip()
        return msg

    def time_since_arrival(self):
        return time.time() - self.time

    def reply(self, message):
        resp = Responce(message, self.user, self.channel)
        return resp

class Responce(object):

    def __init__(self, message, user, channel):
        self.msg = unicode(message)
        self.user = user
        self.channel = channel
        self.length = len(self.render())

    def render(self):
        return getattr(settings, 'RESPONCE_FORMAT', '{user}, {message}').format(user=self.user, message=self.msg)