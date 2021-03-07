import pytest

from promptwithoptions import (
    set_prompt_defaults,
    reset_prompt_defaults,
    promptwithoptions,
)

def test_set_prompt_defaults_prompt():
    reset_prompt_defaults()
    with pytest.raises(TypeError):
        set_prompt_defaults(prompt=8)
    set_prompt_defaults(prompt="who")

def test_set_prompt_defaults_options():
    reset_prompt_defaults()
    with pytest.raises(TypeError):
        set_prompt_defaults(options=8)
    with pytest.raises(TypeError):
        set_prompt_defaults(options='xyz')
    with pytest.raises(TypeError):
        set_prompt_defaults(options=(1,2,2))
    set_prompt_defaults(options=list())
    set_prompt_defaults(options=tuple())
    set_prompt_defaults(options=dict())
    set_prompt_defaults(options=set())

def test_set_prompt_defaults_data_type():
    reset_prompt_defaults()
    with pytest.raises(TypeError):
        set_prompt_defaults(data_type='x')
    set_prompt_defaults(data_type=bool)
    set_prompt_defaults(data_type=lambda x: x)

def test_set_prompt_defaults_options_and_data_type():
    reset_prompt_defaults()
    with pytest.raises(TypeError):
        set_prompt_defaults(options=list(), data_type=bool)
    with pytest.raises(TypeError):
        set_prompt_defaults(options=(1,2,'x'), data_type=int)
    set_prompt_defaults(options=(1,2,3), data_type=int)
    set_prompt_defaults(options=('1','2',3), data_type=int)

def test_set_prompt_defaults_default():
    reset_prompt_defaults()
    set_prompt_defaults(default='x')

def test_set_prompt_defaults_options_and_default():
    reset_prompt_defaults()
    with pytest.raises(TypeError):
        set_prompt_defaults(options=('a', 'b'), default='x')
    set_prompt_defaults(options=('a', 'x'), default='x')

def test_set_prompt_defaults_options_and_default_separately():
    reset_prompt_defaults()
    with pytest.raises(TypeError):
        set_prompt_defaults(options=('a', 'b'), default='x')
    set_prompt_defaults(options=('a', 'b'))
    with pytest.raises(TypeError):
        set_prompt_defaults(default='x')

def test_set_prompt_defaults_data_type_and_default():
    reset_prompt_defaults()
    with pytest.raises(TypeError):
        set_prompt_defaults(data_type=int, default='x')
    set_prompt_defaults(data_type=int, default=2)
    set_prompt_defaults(data_type=int, default='2')
    with pytest.raises(TypeError):
        set_prompt_defaults(data_type=bool, default=1)
    set_prompt_defaults(data_type=bool, default=True)
    set_prompt_defaults(data_type=bool, default='Y')
    set_prompt_defaults(data_type=bool, default='no')
    set_prompt_defaults(data_type=bool, default=(True, False), allow_multiple=True)

def test_set_prompt_defaults_allow_empty():
    reset_prompt_defaults()
    with pytest.raises(TypeError):
        set_prompt_defaults(allow_empty='x')
    set_prompt_defaults(allow_empty=True)

def test_set_prompt_defaults_allow_multiple():
    reset_prompt_defaults()
    with pytest.raises(TypeError):
        set_prompt_defaults(allow_multiple='x')
    set_prompt_defaults(allow_multiple=True)

def test_set_prompt_defaults_show_confirmation():
    reset_prompt_defaults()
    with pytest.raises(TypeError):
        set_prompt_defaults(show_confirmation='x')
    set_prompt_defaults(show_confirmation=True)

def test_set_prompt_defaults_hide_questionmark():
    reset_prompt_defaults()
    with pytest.raises(TypeError):
        set_prompt_defaults(hide_questionmark='x')
    set_prompt_defaults(hide_questionmark=True)

def test_set_prompt_defaults_hide_mandatory_sign():
    reset_prompt_defaults()
    with pytest.raises(TypeError):
        set_prompt_defaults(hide_mandatory_sign='x')
    set_prompt_defaults(hide_mandatory_sign=True)

def test_set_prompt_defaults_hide_multiple_choice_sign():
    reset_prompt_defaults()
    with pytest.raises(TypeError):
        set_prompt_defaults(hide_multiple_choice_sign='x')
    set_prompt_defaults(hide_multiple_choice_sign=True)

def test_set_prompt_defaults_options_line_color():
    reset_prompt_defaults()
    with pytest.raises(TypeError):
        set_prompt_defaults(options_line_color=8)
    set_prompt_defaults(options_line_color="\u001b[37m")

def test_set_prompt_defaults_options_number_color():
    reset_prompt_defaults()
    with pytest.raises(TypeError):
        set_prompt_defaults(options_number_color=8)
    set_prompt_defaults(options_number_color="\u001b[37m")

def test_set_prompt_defaults_input_line_color():
    reset_prompt_defaults()
    with pytest.raises(TypeError):
        set_prompt_defaults(input_line_color=8)
    set_prompt_defaults(input_line_color="\u001b[37m")

def test_set_prompt_defaults_confirm_line_color():
    reset_prompt_defaults()
    with pytest.raises(TypeError):
        set_prompt_defaults(confirm_line_color=8)
    set_prompt_defaults(confirm_line_color="\u001b[37m")

def test_promptwithoptions():
    reset_prompt_defaults()
    with pytest.raises(TypeError):
        promptwithoptions(options=8)
