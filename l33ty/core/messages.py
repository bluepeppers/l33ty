import time
import settings

class Request(object):

    def __init__(self, message, user, channel):
        self.length = len(message)
        message = unicode(message)

        bot_nickname = getattr(settings, 'IRC_NICKNAME', 'l33ty')
        message = message.lstrip(bot_nickname).lstrip()
        self.msg = message
        self.user, _, self.host = user.partition('!')
        self.channel = channel

        self.time = time.time()

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