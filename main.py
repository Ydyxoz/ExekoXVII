# on importe le module discord.py
import discord
import random
import time
import asyncio
import webbrowser


TOKEN = "ODAzNTM3NzA2NzcxNjc3MTk1.YA_Ozg.ZUA6vxuTZn-j9ClU0iRVXrx-yqo"


# créer le bot
client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("H! Hello"):
        await message.channel.send("Hello dear friend, what can I do for you?")

    if message.content.startswith("H! Beer"):
        await message.channel.send("Here is your beer traveler!🍺")

    if message.content.startswith("H! Drunk"):
        await message.channel.send("I cannot give you another beer if you don't succeed"
                                   " to answer to some questions! Take the test on https://quipoquiz.com/fr/index")

    if message.content.startswith("H! Test 1/5"):
        await message.channel.send("Hmm I think you may be too drunk to take another beer. "
                                   "Do you want to order something to eat?🍔🍟")

    if message.content.startswith("H! Test 2/5"):
        await message.channel.send("Hmm I think you may be too drunk to take another beer. "
                                   "Do you want to order something to eat?🍔🍟")

    if message.content.startswith("H! Test 3/5"):
        await message.channel.send("Let's give you a beer for your effort my friend!🍺")

    if message.content.startswith("H! Test 4/5"):
        await message.channel.send("Let's give you a beer for your effort my friend!🍺")

    if message.content.startswith("H! Test 5/5"):
        await message.channel.send("Let's give you a beer for your effort my friend!🍺")

    if message.content.startswith("H! Burger"):
        await message.channel.send("It's a nice idea not to drink too much and eat some food,"
                                   "we care about your health ⛺At the Fireside⛺!")


@client.event
async def on_ready():
    print("ExekoXVII n'est pas du matin")


client.run(TOKEN)
print(client.user.name)
