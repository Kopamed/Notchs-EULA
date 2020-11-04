import os
import random
import asyncio
import json
import discord
from discord.ext import commands
from dotenv import load_dotenv
import datetime
from db import DB



def bot_help(message):
    with open("extras.json", "r") as f:
        extras = json.load(f)
    
    member_rank_perms = "Non"
    
    for group in extras["roles"]:
        
        for guild_role in extras["roles"][group]:
            
            
            for role in message.author.roles:
                if role.id == extras["roles"][group][guild_role]:
                    member_rank_perms = group
                
        
    embed = discord.Embed(title=f"Command prefix = {extras['prefix']}", colour = random.randint(1,16777215), description = f"Commands for {member_rank_perms} perms")
    for i in extras["commands"]:
        embed.add_field(name=i, value=extras["commands"][i])
    
    return embed