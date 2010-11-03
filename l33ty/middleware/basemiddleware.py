class BaseMiddleware(object):
    def msg_in(self, user, message, length):
        raise NotImplementedError('msg_in has not been implemented')

    def msg_out(self, user, message, length):
        raise NotImplementedError('msg_out has not been implemented')