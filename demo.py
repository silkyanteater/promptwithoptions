from promptwithoptions import (
    set_prompt_defaults,
    reset_prompt_defaults,
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

def choice(field, key = None, widget = None, options = None, default = None, allow_empty = None, allow_multiple = None, allow_repetitive = None, hide_key = None):
    result = promptwithoptions(field, options=options, default=default, allow_empty=allow_empty, allow_multiple=allow_multiple, allow_repetitive=allow_repetitive, hide_key=hide_key)
    if widget is not None:
        widget[key] = result
    print()

options = ('Blue', 'Orange', 'White', 'Red', 'Green')
default = 'Orange'
widget = dict()

set_prompt_defaults(options_line_color=CLR.blue, options_number_color=CLR.yellow, input_line_color=CLR.l_blue, confirm_line_color=CLR.l_cyan)
set_prompt_defaults(show_confirmation=True)
# set_prompt_defaults(hide_key=True, hide_mandatory_sign=True, hide_multiple_choice_sign=True)
# set_prompt_defaults(show_confirmation='_None_')

zone_options = {1: 'Header', 2: 'Main area', 3: 'Footer', '': 'Default'}

choice('Zones', 'Zones', widget, options=zone_options, default=(1,2), allow_multiple=True)

choice('Widget Type', 'Type', widget, options, default)

choice('Name', 'Name', widget, default='asdf,asd', allow_empty=True, allow_multiple=True)

choice('Zones', 'Zones', widget, options=zone_options, default=(1,2,''), allow_multiple=True)

choice('Zones', 'Zones', widget, options=zone_options, default=(1,2,''), allow_multiple=True, hide_key=True)

choice('Zones', 'Zones', widget, options=zone_options, default=(1,1,''), allow_multiple=True, allow_repetitive=True, hide_key=True)

# reset_prompt_defaults()
set_prompt_defaults(data_type=bool)

choice('Whether', 'Whether', widget)
choice('Bools', 'Bools', widget, allow_multiple=True)
choice('Bool Series', 'BoolSeries', widget, default=('y', 'y'), allow_multiple=True, allow_repetitive=True)
choice('Bool Series', 'BoolSeries', widget, default='y, y', allow_multiple=True, allow_repetitive=True)

print(widget)
