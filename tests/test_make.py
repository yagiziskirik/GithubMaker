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

MIT_License = f"""MIT License

Copyright (c) {timeNow} {TEST_NAME}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""


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
