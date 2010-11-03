def text_processor(func):
    """
    Replaces request and responce objects with raw strings.
    >>>@text_processor
    ...def view(input):
    ...    assert isinstance(input, basestring)
    ...    return input.replace('.', '-')
    ...
    >>>output = view('-.-')
    >>>assert output == '---'
    """
    def inner(req, **kwargs):
        out = func(req.msg, **kwargs)
        resp = req.reply(req.msg)
        return resp
    return inner