#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# +------------------------------------------------------------------+
# |             ____ _               _        __  __ _  __           |
# |            / ___| |__   ___  ___| | __   |  \/  | |/ /           |
# |           | |   | '_ \ / _ \/ __| |/ /   | |\/| | ' /            |
# |           | |___| | | |  __/ (__|   <    | |  | | . \            |
# |            \____|_| |_|\___|\___|_|\_\___|_|  |_|_|\_\           |
# |                                                                  |
# | Copyright Mathias Kettner 2014             mk@mathias-kettner.de |
# +------------------------------------------------------------------+
#
# This file is part of Check_MK.
# The official homepage is at http://mathias-kettner.de/check_mk.
#
# check_mk is free software;  you can redistribute it and/or modify it
# under the  terms of the  GNU General Public License  as published by
# the Free Software Foundation in version 2.  check_mk is  distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
# out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
# PARTICULAR PURPOSE. See the  GNU General Public License for more de-
# tails. You should have  received  a copy of the  GNU  General Public
# License along with GNU Make; see the file  COPYING.  If  not,  write
# to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
# Boston, MA 02110-1301 USA.

from cmk.gui.i18n import _
from cmk.gui.valuespec import (
    Age,
    Dictionary,
    TextAscii,
    Tuple,
)
from cmk.gui.plugins.wato import (
    RulespecGroupCheckParametersEnvironment,
    register_check_parameters,
)

register_check_parameters(
    RulespecGroupCheckParametersEnvironment,
    "siemens_plc_duration",
    _("Siemens PLC Duration"),
    Dictionary(
        elements=[
            ('duration',
             Tuple(
                 title=_("Duration"),
                 elements=[
                     Age(title=_("Warning at"),),
                     Age(title=_("Critical at"),),
                 ])),
        ],
        help=_("This rule is used to configure thresholds for duration values read from "
               "Siemens PLC devices."),
        title=_("Duration levels"),
    ),
    TextAscii(
        title=_("Device Name and Value Ident"),
        help=_("You need to concatenate the device name which is configured in the special agent "
               "for the PLC device separated by a space with the ident of the value which is also "
               "configured in the special agent."),
    ),
    match_type="dict",
)
