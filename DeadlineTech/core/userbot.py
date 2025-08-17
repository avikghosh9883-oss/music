

# ==========================================================
# 🎧 Public Open-Source VC Player Music Bot (Cookies Based)
# 🛠️ Maintained by Team DeadlineTech | Lead Developer: @Its_damiann
# 🔓 Licensed for Public Use — All Rights Reserved © Team DeadlineTech
#
# This file is part of a publicly available and open-source Telegram music bot
# developed by Team DeadlineTech. It offers high-quality streaming in Telegram voice
# chats using YouTube as a source, supported by session-based assistant accounts and
# YouTube cookie integration for improved access and performance.
#
# 💡 This source code is released for educational and community purposes. You're free
# to study, modify, and deploy it under fair and respectful usage. However, any misuse,
# removal of credits, or false ownership claims will be considered a violation of our
# community standards and may lead to denial of support or blacklisting.
#
# 🔗 Looking for powerful performance with stable APIs? Get access to the official
# premium API service: https://DeadlineTech.site
#
# ❤️ Openly built for the community, but proudly protected by the passion of its creators.
# ==========================================================



from pyrogram import Client
import config
from ..logging import LOGGER

assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="DeadlineXAss1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            name="DeadlineXAss2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            name="DeadlineXAss3",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            name="DeadlineXAss4",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            name="DeadlineXAss5",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info("🚀 Starting assistant clients...")

        async def setup_assistant(client, number):
            try:
                await client.start()
                await client.join_chat("DeadlineTechTeam")
                await client.join_chat("DeadlineTechSupport")
            except Exception:
                pass

            assistants.append(number)

            try:
                await client.send_message(config.LOGGER_ID, f"✅ My Assistant {number} is now online.")
            except Exception:
                LOGGER(__name__).error(
                    f"❌ Assistant {number} failed to send a message to the log group. "
                    f"Ensure it's added and promoted to admin in LOGGER group ({config.LOGGER_ID})."
                )
                exit()

            client.id = client.me.id
            client.name = client.me.mention
            client.username = client.me.username
            assistantids.append(client.id)

            LOGGER(__name__).info(f"🤖 Assistant {number} is active as {client.name}")

        if config.STRING1:
            await setup_assistant(self.one, 1)
        if config.STRING2:
            await setup_assistant(self.two, 2)
        if config.STRING3:
            await setup_assistant(self.three, 3)
        if config.STRING4:
            await setup_assistant(self.four, 4)
        if config.STRING5:
            await setup_assistant(self.five, 5)

        LOGGER(__name__).info("✅ All available assistants are now online.")

    async def stop(self):
        LOGGER(__name__).info("🛑 Shutting down assistant clients...")
        try:
            if config.STRING1:
                await self.one.stop()
            if config.STRING2:
                await self.two.stop()
            if config.STRING3:
                await self.three.stop()
            if config.STRING4:
                await self.four.stop()
            if config.STRING5:
                await self.five.stop()
        except Exception as e:
            LOGGER(__name__).warning(f"⚠️ Error while stopping assistants: {e}")
