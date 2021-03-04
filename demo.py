from promptwithoptions import (
    set_prompt_defaults,
    promptwithoptions,
)

class CLR(object):
    reset = '\u001b[0m'
    black = '\u001b[30m'
    red = '\u001b[31m'
    green = '\u001b[32m'
    yellow = '\u001b[33m'
    blue = '\u001b[34m'
    magenta = '\u001b[35m'
    cyan = '\u001b[36m'
    white = '\u001b[37m'
    l_black = '\u001b[30;1m'
    l_red = '\u001b[31;1m'
    l_green = '\u001b[32;1m'
    l_yellow = '\u001b[33;1m'
    l_blue = '\u001b[34;1m'
    l_magenta = '\u001b[35;1m'
    l_cyan = '\u001b[36;1m'
    l_white = '\u001b[37;1m'

def choice(field, key, widget, options, default = None):
    widget[key] = promptwithoptions(field, options=options, default=default)

options = ('InternalLinkBanner', 'ExternalLinkBanner', 'OddsBanner', 'Cardbanner', 'OTCCouponDetail')
default = 'ExternalLinkBanner'
widget = dict()

set_prompt_defaults(show_confirmation=True, options_line_color=CLR.blue, options_number_color=CLR.yellow, input_line_color=CLR.l_blue, confirm_line_color=CLR.l_cyan)

choice('Widget Type', 'Type', widget, options, default)
print(widget)
