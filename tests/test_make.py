# Copyright (c) 2023 Yağız Işkırık
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import GithubMaker.make as gm
from datetime import datetime
import pytest
import builtins


timeNow = datetime.now().year
TEST_NAME = "John Doe"


# Input Faker
input_values = []
print_values = []


def mock_input(s):
    print_values.append(s)
    return input_values.pop(0)


def mock_input_output_start():
    global input_values, print_values

    input_values = []
    print_values = []

    builtins.input = mock_input
    builtins.print = lambda s: print_values.append(s)


def get_display_output():
    global print_values
    return print_values


def set_keyboard_input(mocked_inputs):
    global input_values

    mock_input_output_start()
    input_values = mocked_inputs


# LICENSE GENERATION TESTS
ISC_License = f"""ISC License

Copyright (c) {timeNow} {TEST_NAME}

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE."""

MIT_License = f"""ISC License

Copyright (c) {timeNow} {TEST_NAME}

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE."""


@pytest.mark.parametrize('licenseType, name, result', [
    ('ISC', TEST_NAME, ISC_License),
    ('MIT', TEST_NAME, MIT_License)
])
def test_license_generation(licenseType, name, result):
    assert gm.Templates('', '', '', name, '', licenseType).getLicense() == result


@pytest.mark.parametrize('userInput, value, expected', [
    ('', True, True),
    ('', False, False),
    ('y', True, True),
    ('y', False, True),
    ('Y', True, True),
    ('Y', False, True),
    ('n', True, False),
    ('n', False, False),
    ('N', True, False),
    ('N', False, False)
])
def test_editVar(userInput, value, expected):
    newGm = gm.GithubMaker()
    set_keyboard_input([userInput])
    returnVal = newGm.editVar("Test", value)
    assert returnVal == expected


@pytest.mark.parametrize('userInput, value, expected', [
    ('Test', 'Test', 'Test'),
    ('', 'Test', 'Test'),
    ('Empty', 'Test', 'Empty'),
    ('Long expected string', 'Default', 'Long expected string'),
    ('@@@', '@@', '@@@'),
    ('', '@@', '@@')
])
def test_changeIfNotEmpty(userInput, value, expected):
    newGm = gm.GithubMaker()
    set_keyboard_input([userInput])
    returnVal = newGm.changeIfNotEmpty("Test", value)
    assert returnVal == expected
