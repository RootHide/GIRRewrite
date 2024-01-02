import asyncio
import os

import mongoengine
from dotenv import find_dotenv, load_dotenv

from data.model.guild import Guild

load_dotenv(find_dotenv())

async def setup():
    print("STARTING SETUP...")
    guild = Guild()

    # you should have this setup in the .env file beforehand
    guild._id          = int(os.environ.get("MAIN_GUILD_ID"))

    # If you're re-running this script to update a value, set case_id
    # to the last unused case ID or else it will start over from 1!
    guild.case_id      = 1

    # required for permissions framework!
    guild.role_administrator = 1156629535656255542
    guild.role_moderator     = 1191601804606197860
    guild.role_birthday      = 1191604372652695643
    guild.role_genius        = 1190914822032855090
    guild.role_dev           = 1155579868772302939
    guild.role_memberone     = 1191604006594822195
    guild.role_memberedition = 1160485769207615578
    guild.role_memberpro     = 1191603410710040577
    guild.role_memberplus    = 1191603483804172368
    guild.role_memberultra   = 1191604141680767095

    guild.channel_reports        = 1191604871690981386
    # channel where reactions will be logged
    guild.channel_emoji_log      = 1191605083549487154
    # channel for private mod logs
    guild.channel_private        = 1191605192957890653
    # rules-and-info channel
    guild.channel_rules          = 1162752219632914432
    # channel for public mod logs
    guild.channel_public         = 1191605566137716766
    # optional, required for /issue command
    guild.channel_common_issues  = 1159085637501202513
    # #general, required for permissions
    guild.channel_general        = 1190912735228199033
    # required for filter
    guild.channel_development    = 1190879087045115974
    # required, #bot-commands channel
    guild.channel_botspam        = 1191605893717053540

    # you can fill these in if you want with IDs, or you ca use commands later
    guild.logging_excluded_channels = []  # put in a channel if you want (ignored in logging)
    guild.filter_excluded_channels  = []  # put in a channel if you want (ignored in filter)
    guild.filter_excluded_guilds    = []  # put guild ID to whitelist in invite filter if you want

    guild.nsa_guild_id = 123 # you can leave this as is if you don't want Blootooth (message mirroring system)

    guild.save()
    print("DONE")

if __name__ == "__main__":
    if os.environ.get("DB_CONNECTION_STRING") is None:
        mongoengine.register_connection(
            host=os.environ.get("DB_HOST"), port=int(os.environ.get("DB_PORT")), alias="default", name="botty")
    else:
        mongoengine.register_connection(
            host=os.environ.get("DB_CONNECTION_STRING"), alias="default", name="botty")
    res = asyncio.get_event_loop().run_until_complete( setup() )
