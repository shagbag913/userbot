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
async def rtreplacer(message):
    text = message.text
    replacement_keys = replacements.keys()
    for replacement in replacement_keys:
        if replacement in text:
            text = text.replace(replacement, replacements[replacement])
    await message.edit(text)
