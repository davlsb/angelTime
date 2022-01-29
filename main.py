import discord
import os
import time
from threading import Timer
from datetime import datetime
from pytz import timezone
from keepAlive import keep_alive

client = discord.Client()
channel_id = os.environ['ID'] #replace with Channel ID of the channel where the messages are sent
token = os.environ['TOKEN'] #replace with bot token, which is found in Discord developer setting

eastern = timezone('US/Eastern')

timeout = 59

keep_alive()

def time_module():
    print("time module in use")
    while True:
        current_time = datetime.now(eastern).strftime("%H:%M")
        print(current_time)
        if (current_time == "01:11" or current_time == "02:22"
                or current_time == "03:33" or current_time == "04:44"
                or current_time == "05:55" or current_time == "13:11"
                or current_time == "14:22" or current_time == "15:33"
                or current_time == "16:44" or current_time == "17:55"
                or current_time == "11:11"):
            print("time module ended")
            break


keep_alive()
time_module()


@client.event
async def on_ready():
    print("bot:user ready == {0.user}".format(client))
    channel = client.get_channel(channel_id)
    await channel.send("Make a Wish, the angels are listening")
    print("waiting 60 seconds")
    angel_message()


def angel_message():
    @client.event
    async def on_message(message):
        t = Timer(timeout, print, ['Sorry, times up'])
        t.start()
        if message.author == client.user:
            return
        if message.content.startswith('Angel') or message.content.startswith(
                'angel') or message.content.startswith(
                    'I wish') or message.content.startswith('i wish'):
            await message.channel.send(
                'An angel was sent to grant your wish ^-^')
        time_module()


keep_alive()
client.run(token)




