import os
import random
import asyncio
import json
import discord
from discord.ext import commands
from dotenv import load_dotenv
import datetime
from db import DB
from bruh import *

load_dotenv()
TOKEN = os.getenv('token')
db = DB()
client = discord.Client()




@client.event
async def on_ready():
    with open("extras.json", "r") as f:
        extras = json.load(f)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=random.choice(extras["statuses"]) + extras["main_status"]))
    
    print(f'{client.user} has connected to Discord!')
    



@client.event
async def on_member_join(member):
    db.add_employee(member)
    





@client.event
async def on_reaction_add(reaction, user):
    pass




@client.event
async def on_reaction_remove(reaction, user):
    pass



@client.event
async def on_message(message):
    with open("extras.json", "r") as f:
        extras = json.load(f)
    if message.content == "":
        return
    
   

    message_lower = message.content.lower()
    
    
    end = len(extras["prefix"])
    if message_lower[0:end] == extras["prefix"]:
        if message_lower[end:] != "":
            command = message_lower[end:]
            #await message.channel.send(command)
            
        else:
            await message.channel.send(content=None, embed = bot_help(message))
            return
        
            
        if command in extras["commands"]["all"]:
            
            
            if command == "help":
                embed = discord.Embed(title=f"Command prefix = {extras['prefix']}", colour = random.randint(1,16777215))
                for i in extras["commands"]["all"]:
                    embed.add_field(name=i, value=extras["commands"]["all"][i])
                await message.channel.send(content=None, embed = embed)
                return
                
                
            
            elif command == "speak":
                await message.channel.send("fuck")
                
            
            
            
            else:
                embed = discord.Embed(title=f"Coming Soon!", colour = random.randint(1,16777215))
                embed.add_field(name="This command is unavailable", value="This command is currently unavailable, but will be available soon")
                await message.channel.send(content=None, embed = embed)
                return
                
    
    
    
    
    

client.run(TOKEN)