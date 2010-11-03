from . import BaseMiddleware

import re


class NumberToBinaryMiddleware(BaseMiddleware):
    """
    Converts any numbers being sent to their binary representation
    """

    def msg_in(self, user, message, length):
        """Don't modify incoming messages"""
        return {'message': message, 'user': user, 'length': length}

    def msg_out(self, user, message, length):
        message = self.filter_msg(message)
        return {'message': message, 'user': user, 'length': length}

    def filter_msg(self, msg):
        raw_regex = '(\d+)'
        regex = re.compile(raw_regex)

        new_msg = ''
        unfiltered_msg = list(msg)
        while 1:
            match = regex.search(''.join(unfiltered_msg))
            
            if match is None:
                new_msg += ''.join(unfiltered_msg)
                break

            start, end = match.span()

            base_10 = int(''.join(unfiltered_msg[start:end]))
            base_2 = self.int2bin(base_10)

            filtered_msg = unfiltered_msg[:start]
            filtered_msg.append(base_2)

            new_msg += ''.join(filtered_msg)
            unfiltered_msg = unfiltered_msg[end:]
        return new_msg

    @staticmethod
    def int2bin(n, count=24):
        """returns the binary of integer n, using count number of digits"""
        return "".join([str((n >> y) & 1) for y in range(count-1, -1, -1)]).lstrip('0')
