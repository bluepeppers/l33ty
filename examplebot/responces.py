def add(req, first, second):
    try:
        first = int(first)
        second = int(second)
    except:
        return req.reply('Thoes don\'t seem to be valid ints')
    else:
        return req.reply('{0} + {1} = {2}'.format(first, second, first + second))