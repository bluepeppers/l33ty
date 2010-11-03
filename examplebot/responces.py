from math import *

def calculator(req, term):
    if sum(term.find(c) for c in ';\n') > 0:
        return req.reply('Please do _not_ use compond statements')
    else:
        try:
            out = eval(term)
        except Exception as e:
            return req.reply('Error: {0}'.format(e))
        else:
            return req.reply(out)