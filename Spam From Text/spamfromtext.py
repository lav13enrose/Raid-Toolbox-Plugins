# Plugin Author: lav13enrose
# Plugin Name: Random Pick Line from File
# Date: 69/69/2069

import discord
import random
import sys

client = discord.Client()
token = sys.argv[1]
SERVER = sys.argv[2]
chan = sys.argv[3]
fileinput = sys.argv[4]

@client.event
async def on_ready():
    server = client.get_guild(int(SERVER))
    channellist = []
    memberlist = []
    import random
    txtchan = client.get_channel(int(chan))
    while not client.is_closed():
        message = ''
        for x in range(1):
            message += random.choice(open(fileinput).readlines())
        await txtchan.send(message)

client.run(token, bot=False)
