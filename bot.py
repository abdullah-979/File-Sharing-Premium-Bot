from aiohttp import web
from plugins import web_server
import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime
from config import *
import pyrogram.utils

pyrogram.utils.MIN_CHANNEL_ID = -1009999999999

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=API_ID,
            plugins={"root": "plugins"},
            workers=TG_BOT_WORKERS,
            bot_token=BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()
        self.username = usr_bot_me.username

        # Function to export invite link and set it as an attribute
        async def set_invite_link(channel, attr_name):
            try:
                chat = await self.get_chat(channel)
                link = chat.invite_link
                if not link:
                    link = await self.export_chat_invite_link(channel)
                setattr(self, attr_name, link)
            except Exception as e:
                self.LOGGER(__name__).warning(e)
                self.LOGGER(__name__).warning(f"Bot Can't Export Invite Link from Force Sub Channel {channel}!")
                self.LOGGER(__name__).warning(f"Please Double Check The {channel} Value And Ensure The Bot Is Admin In The Channel With 'Invite Users Via Link' Permission.")
                self.LOGGER(__name__).info("Bot Stopped.")
                sys.exit()

        # Set invite links for all force subscription channels
        if FORCE_SUB_CHANNEL:
            await set_invite_link(FORCE_SUB_CHANNEL, 'invitelink')
        if FORCE_SUB_CHANNEL2:
            await set_invite_link(FORCE_SUB_CHANNEL2, 'invitelink2')
        if FORCE_SUB_CHANNEL3:
            await set_invite_link(FORCE_SUB_CHANNEL3, 'invitelink3')
        if FORCE_SUB_CHANNEL4:
            await set_invite_link(FORCE_SUB_CHANNEL4, 'invitelink4')

        # Check and set the DB channel
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test_message = await self.send_message(chat_id=db_channel.id, text="Hey 🖐")
            await test_message.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(f"Make Sure The Bot Is Admin In The DB Channel, And Double Check The CHANNEL_ID Value, Current Value: {CHANNEL_ID}")
            self.LOGGER(__name__).info("Bot Stopped.")
            sys.exit()

        # Set parse mode
        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info("Bot Running..!")

        # Start web server
        app_runner = web.AppRunner(await web_server())
        await app_runner.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app_runner, bind_address, PORT).start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot Stopped...")

