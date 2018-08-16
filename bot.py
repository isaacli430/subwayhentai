import discord
from discord.ext import commands

class IAGREEWITHMYHUSBAND(commands.Bot):

    def __init__(self):
        super().__init__(command_prefix="!")

    async def on_message(self, message):
        if "<@450193316076584960>" in message.content:
            await message.channel.send(f"I agree with my husband ({message.author.mention})")

    async def on_ready(self):
        print("ready")

IAGREEWITHMYHUSBAND().run("NDUwMTkzMzE2MDc2NTg0OTYw.DlcLdw.EUoCUHrMf0ma6bDKgewLy-UhIw8", bot=False)