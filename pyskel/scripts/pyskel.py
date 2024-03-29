#!/usr/bin/env python
# -*- coding: utf8 -*-
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Main script for pyskel.

:copyright:
    2021 Author Name <author@email.com>
:license:
    GNU General Public License v3.0 or later
    (https://www.gnu.org/licenses/gpl-3.0-standalone.html)
"""
import sys
import argparse
from .._version import get_versions
from ..utils import (
    parse_configspec, read_config, validate_config, write_sample_config
)


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='Run pyskel.')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        '-c', '--configfile', type=str,
        help='config file for data sources and processing params')
    group.add_argument(
        '-s', '--sampleconfig', default=False, action='store_true',
        required=False,
        help='write sample config file to current directory and exit')
    parser.add_argument(
        '-v', '--version', action='version',
        version='%(prog)s {}'.format(get_versions()['version']))
    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()
    configspec = parse_configspec()
    if args.sampleconfig:
        write_sample_config(configspec, 'pyskel')
        sys.exit(0)
    config = read_config(args.configfile, configspec)
    validate_config(config)
    print(config)
