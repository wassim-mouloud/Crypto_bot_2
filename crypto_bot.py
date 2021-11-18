import disnake
import os
from disnake.ext import commands
from crypto_functions import *

#CMC_API_KEY=os.environ.get('CMC')
#token=os.environ.get('Discord_crypto_bot_token')
client = commands.Bot(command_prefix='.',intents=disnake.Intents.all(), activity=disnake.Game(name='SHIB is going to 0'))

@client.event
async def on_ready():
    print("Hey I am ready ")

@client.event 
async def on_member_join(member):
    await member.send("Hello, you're not welcome here get out of my server!!! 😘")


@client.event
async def on_message(message):
    id=client.get_guild(889583100286369832)
    if str(message.channel)=='bot_commands':
        try:
            if message.content.startswith('!'):
                crypto_to_check=message.content.split("!")[1].lower()
                await message.channel.send(get_crypto_price(crypto_to_check))
        except:
            await message.channel.send(f"sorry couldn't find {crypto_to_check} ")

    if message.content=="hello":
        await message.author.send("Hi hope you're having a great day")
            
    await client.process_commands(message)
#this function checks if the command is being executed in the right channel
def check_channel(ctx):
    if str(ctx.channel)=='bot_commands' or str(ctx.channel)=="🤖bot_commands" or str(ctx.channel)=="🤖 bot_commands":
        return True
#get crypto price
@client.command()
@commands.check(check_channel)
async def price(ctx,crypto):
    try:
        embed=disnake.Embed(title=get_crypto_price(crypto.lower()), color=disnake.Color.blue())
        await ctx.send(embed=embed)
    except:
        await ctx.send(f"sorry I don't know what {crypto} is ")
#get crypto rank according to market cap
@client.command()
@commands.check(check_channel)
async def rank(ctx,crypto):
    try:
        await ctx.send(get_crypto_rank(crypto.lower()))
    except:
        await ctx.send(f"sorry I don't know what {crypto} is ")
@client.command()
@commands.check(check_channel)  
async def position(ctx,crypto_rank):
    try:
        await ctx.send(get_crypto_rank2(crypto_rank))  
    except:
        await ctx.send(f"sorry I don't know what {crypto} is ")
#get crypto price with symbol
@client.command()
@commands.check(check_channel)
async def sym_price(ctx,crypto):
    try:
        embed=disnake.Embed(title=get_price_with_symbol(crypto.upper()),color=disnake.Color.green())
        await ctx.channel.send(embed=embed)
    except:
        await ctx.send(f"sorry I don't know what {crypto} is ")
#get a 24h performance of an asset
@client.command()
@commands.check(check_channel)
async def perf24h(ctx,crypto):
        await ctx.channel.send(get_performance_24(crypto.lower()))
@client.command()
@commands.check(check_channel)
async def perf7d(ctx,crypto):
    try:
        await ctx.send(get_performance_7d(crypto.lower()))
    except:
        await ctx.send(f"sorry I don't know what {crypto} is ")
#this command is just for fun    
@client.command()
@commands.check(check_channel)
async def sido(ctx):
    embed=disnake.Embed(title='everytime you use this command sido pays a predefined fee of 0.05$ \nhttps://sidoexe.web.app/',color=disnake.Color.blue())
    await ctx.channel.send(embed=embed)
    
#moderator command to clear spam
@client.command()
async def clear(ctx,amount):
    await ctx.channel.purge(limit=int(amount))
#get all info on a specific crypto
@client.command()
@commands.check(check_channel)
async def everything(ctx,crypto):
    try:
        await ctx.channel.send(get_everything_about_the_crypto(crypto.lower()))
    except:
        await ctx.send(f"sorry I don't know what {crypto} is")
#this command gives general info about a crypto like what this crypto is and gives the main website of the crypto
@client.command()
@commands.check(check_channel)
async def info(ctx,crypto):
    try:
        await ctx.channel.send(get_crypto_info(crypto.lower()))
    except:
        await ctx.send(f"sorry I don't know what {crypto} is ")
#this command gives the link to any crypto's reddit
@client.command()
@commands.check(check_channel)
async def reddit(ctx,crypto):
    try:
        embed=disnake.Embed(title=get_crypto_reddit(crypto.lower()),color=disnake.Color.green())
        await ctx.channel.send(embed=embed)
    except:
        await ctx.send(f"sorry I don't know what {crypto} is ")
#personal command non related to crypto    
@client.command()
async def ping(ctx):
    guild=ctx.guild
    sido=guild.get_member(439800066312503297)
    raff=guild.get_member(401050345716973569)
    wass=guild.get_member(396607194910556162)
    if str(ctx.author)=='wass#1670':
        await ctx.send(sido.mention)
        await ctx.send(raff.mention)
    elif str(ctx.author)=='SIDO#4076':
        await ctx.send(raff.mention)
        await ctx.send(wass.mention)
    else:
        await ctx.send(wass.mention)
        await ctx.send(sido.mention)
#price target command
@client.command()
@commands.check(check_channel)
async def target_above(ctx,crypto,price):
    current_price=get_crypto_price_in_numbers_only(crypto.lower())
    if float(current_price)<float(price):
        await ctx.send(f"Hey {ctx.author.mention} I will notify you when {crypto.title()}'s price is trading above or equal to {price}$ ")
    elif float(current_price)>=float(price):
        await ctx.send(f"{ctx.author.mention} {crypto.title()}'s price is trading at {current_price}$ ")
@client.command()
@commands.check(check_channel)
async def target_below(ctx,crypto,price):
    current_price=get_crypto_price_in_numbers_only(crypto.lower())
    if float(current_price)>float(price):
        await ctx.send(f"Hey {ctx.author.mention} I will notify you when {crypto.title()}'s price is trading below or equal to {price}$ ")
    elif float(current_price)<=float(price):
        await ctx.send(f"{ctx.author.mention} {crypto.title()}'s price is trading at {current_price}$ ")

@client.command()
@commands.check(check_channel)
async def top10(ctx):
    top_10 = get_top10()
    file_to_send=''
    for x,y in top_10.items():
        file_to_send+=y
        file_to_send+=':'
        file_to_send+=get_crypto_price_in_numbers_only(top_10[x])+'$'
        file_to_send+='\n'
        file_to_send+='\n'
    embed=disnake.Embed(title=file_to_send, color=disnake.Color.blue() )
    await ctx.send(embed=embed)
client.run('ODg5MTEzNjIwMDUzNjM1MTEy.YUchlQ.klGEloHxDfzt_1mHb8iecGFD6j0')








