
#Url of irc server than l33ty should run on
IRC_HOST = "irc.freenode.net"

#Port of irc server that l33ty should run on
IRC_PORT = 6667

#Channels that l33ty should be in
IRC_CHANNELS = ["#testingbot",]

ROOT_ROUTECONF = 'examplebot.routes'

IRC_NICKNAME = 'l33ty'
ACTIVATION_PREFIX = '|'

try:
    from localsettings import *
except ImportError:
    pass