# Copyright (C) 2019 shagbag913.
#
# Licensed under the Raphielscape Public License, Version 1.b (the "License");
# you may not use this file except in compliance with the License.
#
""" Auto-bans/kicks/mutes/whatever rule breakers """

from userbot import LOGGER, LOGGER_GROUP
from userbot.events import register

replacements = {
    '.SHG': '¯\_(ツ)_/¯',
    '.SWORD': 'o()xxxx[{::::::::::::::::::>',
    '.PFFT': '[¬º-°]¬',
    '.ROLLEYES': '  (◔_◔)',
    '.KILL': '  (⌐■_■)︻╦╤─ (╥﹏╥)'
}

@register(outgoing=True)
async def replacer(message):
    oldtext = message.text
    newtext = message.text
    replacement_keys = replacements.keys()
    for replacement in replacement_keys:
        if replacement in newtext:
            newtext = newtext.replace(replacement, replacements[replacement])
    if newtext != oldtext:
        await message.edit(newtext)
