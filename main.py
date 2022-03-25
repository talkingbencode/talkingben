import discord
import random


ben = [
    "https://cdn.discordapp.com/attachments/941414137978843176/952669091401977916/ben.mp4",
    "https://cdn.discordapp.com/attachments/941414137978843176/952669156128464937/ben.mp4",
    "https://cdn.discordapp.com/attachments/941414137978843176/952669195517194280/ben.mp4",
    "https://cdn.discordapp.com/attachments/941414137978843176/952669279357128704/ben.mp4"
]

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name="YOUR STATUS"))
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$ben '):
        await message.channel.send(random.choice(ben))

        
    if message.content.startswith('$drink'):
        await message.channel.send('https://c.tenor.com/hdPVLfpe81cAAAAC/talking-ben-drinking.gif')


    if message.content.startswith('$beans'):
        await message.channel.send('https://c.tenor.com/UZOcqAyMu4QAAAAd/talking-ben-eating.gif')

    if message.content.startswith('$servers'):
        await message.channel.send("I'm in " + str(len(client.guilds)) + " servers!")

    if message.content.startswith('$invite'):
        await message.channel.send('https://discord.com/api/oauth2/authorize?client_id=953824131579801640&permissions=8&scope=bot')

    if message.content.startswith('$support'):
        await message.channel.send('https://discord.gg/p2WyWSQuVB')

    if message.content.startswith('$help'):
        await message.channel.send('`$ben (question) - Give question to ben`')
        await message.channel.send('`$drink - ben needs a drink`') 
        await message.channel.send('`$beans - give ben some fresh beans`') 
        await message.channel.send('`$servers - see how many server im in`')
        await message.channel.send('`$invite - invite me`') 
        await message.channel.send('`$support - support server`') 

  
client.run('TOKEN')
