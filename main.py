import os
from keep_alive import keep_alive

os.system('pip install discord')
import discord
from discord.ext import commands

token = os.environ['token']   # Enter token in secrets

intents = discord.Intents.default()
intents.members = True

wauv = commands.Bot(command_prefix="-",
                    self_bot=True,
                    case_insensitive=True,
                    intents=intents,
                    help_command=None)

GUILD_ID = PASTE_YOUR_GUILD_ID   # Paste the Guild ID of the server
CHANNEL_ID = PASTE_YOUR_CHANNEL_ID   # Paste the Channel ID of the channel


@wauv.event
async def on_ready():
    os.system('clear')
    print(f'Logged in as {wauv.user} ({wauv.user.id})')
    vc = discord.utils.get(wauv.get_guild(GUILD_ID).channels, id=CHANNEL_ID)
    await vc.guild.change_voice_state(channel=vc,
                                      self_mute=False,   # Toggle mute
                                      self_deaf=False)   # Toggle deafen
    print(f"Successfully joined {vc.name} ({vc.id})")

keep_alive()

wauv.run(token, bot=False)
