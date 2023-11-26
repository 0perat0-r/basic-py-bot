import discord
from discord.ext import commands
import config

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
  print(f'We have logged in as {bot.user}')


@bot.command()
async def ping(ctx):
  await ctx.send('Pong!')
  




print(config.token)