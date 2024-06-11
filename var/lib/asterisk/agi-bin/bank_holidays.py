#!/usr/bin/env python3

import json
import re

import datetime
from jours_feries_france import JoursFeries
from xivo import agi

agi = agi.AGI()

def main():
    """ Bank holidays script"""

    try:
        agi.verbose("Start Bank holidays script")
    except AGIAppError as e:
        print(e)

    # Set default dest -> continue
    destContext = ""
    destExt = "none"

    # Get current date
    now = datetime.date.today()

    # get called number for did matching rule
    callee = agi.get_variable('XIVO_DSTNUM')

    # Check if today is bank holiday
    if JoursFeries.is_bank_holiday(now, zone="Métropole"):
        agi.verbose("Today is bank holiday")
        destContext = "ctx-DEMOFMWdef-internal-6befd0be-faba-496a-8593-6de31e098e51"
        destExt = "*10"
    else:
        agi.verbose("Today is not bank holiday")

    agi.verbose(destContext)
    agi.verbose(destExt)
    agi.set_variable('dest-context', destContext)
    agi.set_variable('dest-ext', destExt)


if __name__ == "__main__": 
    main() 