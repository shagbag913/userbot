# Copyright (C) 2019 shagbag913.
#
# Licensed under the Raphielscape Public License, Version 1.b (the "License");
# you may not use this file except in compliance with the License.
#
""" Auto-bans/kicks/mutes/whatever rule breakers """

from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights

from userbot import LOGGER, LOGGER_GROUP
from userbot.events import register

KEYWORDS = [
    'binance'
]

@register(incoming=True)
async def keyword_banner(message):
    text = message.text
    chat = await message.get_chat()
    chat_id = message.chat_id
    sender_id = message.sender_id
    admin = chat.admin_rights
    creator = chat.creator
    banned_spam = False
    rights = ChatBannedRights(
        until_date=None,
        view_messages=True,
        send_messages=True,
        send_media=True,
        send_stickers=True,
        send_gifs=True,
        send_games=True,
        send_inline=True,
        embed_links=True,
    )

    # Can't ban someone if ya aren't admin :P
    if not admin and not creator:
        return

    # Ban
    for keyword in KEYWORDS:
        if keyword in text.lower():
            try:
                await message.delete()
                await message.client(EditBannedRequest(chat_id, sender_id, rights))
                banned_spam = True
            except:
                pass

            if LOGGER:
                await message.client.send_message(
                    LOGGER_GROUP,
                    "Suspected bot detected.\n - group: `{}`\n - bot ID: `{}`" \
                            "\n - banned: `{}`\n - reason: keyword `{}`".format(
                            chat_id, sender_id, banned_spam, keyword)
                )
            
            # no need to keep checking if they got banned
            if banned:
                return
