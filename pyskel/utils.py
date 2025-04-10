# -*- coding: utf-8 -*-
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Utility functions for pyskel.

:copyright:
    2022 Author Name <author@email.com>
:license:
    GNU General Public License v3.0 or later
    (https://www.gnu.org/licenses/gpl-3.0-standalone.html)
"""
import os
import sys
from .configobj import ConfigObj, ParseError
from .configobj.validate import Validator


def err_exit(msg):
    """
    Print an error message and exit the program.
    """
    sys.stderr.write(f'{msg}\n')
    sys.exit(1)


def parse_configspec():
    """
    Parse the configuration specification file.
    """
    curdir = os.path.dirname(__file__)
    configspec_file = os.path.join(curdir, 'conf', 'configspec.conf')
    return read_config(configspec_file)


def write_ok(filepath):
    """
    Check if the file already exists and prompt the user for confirmation
    to overwrite it.
    """
    if os.path.exists(filepath):
        ans = input(
            f'"{filepath}" already exists. Do you want to overwrite it? [y/N] '
        )
        return ans in ['y', 'Y']
    return True


def write_sample_config(configspec, progname):
    """
    Write a sample configuration file based on the provided configspec.
    """
    c = ConfigObj(configspec=configspec, default_encoding='utf8')
    val = Validator()
    c.validate(val)
    c.defaults = []
    c.initial_comment = configspec.initial_comment
    c.comments = configspec.comments
    c.final_comment = configspec.final_comment
    configfile = f'{progname}.conf'
    if write_ok(configfile):
        with open(configfile, 'wb') as fp:
            c.write(fp)
        print(f'Sample config file written to: "{configfile}"')


def read_config(config_file, configspec=None):
    """
    Read a configuration file and return a ConfigObj object.
    """
    kwargs = dict(
        configspec=configspec, file_error=True, default_encoding='utf8')
    if configspec is None:
        kwargs.update(
            dict(interpolation=False, list_values=False, _inspec=True))
    try:
        config_obj = ConfigObj(config_file, **kwargs)
    except IOError as err:
        err_exit(err)
    except ParseError as err:
        msg = f'Unable to read "{config_file}": {err}'
        err_exit(msg)
    return config_obj


def validate_config(config_obj):
    """
    Validate the configuration object against its configspec.
    """
    val = Validator()
    test = config_obj.validate(val)
    if isinstance(test, dict):
        for entry in test:
            if not test[entry]:
                sys.stderr.write(
                    f'Invalid value for "{entry}": "{config_obj[entry]}"\n')
        sys.exit(1)
    if not test:
        err_exit('No configuration value present!')
