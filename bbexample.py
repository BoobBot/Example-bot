from discord.ext import commands
import os
import json

with open('config.json') as config:
    config = json.load(config)

bot = commands.AutoShardedBot(command_prefix=config['prefix'], description='An example bot for bb api')
bot.config = config

for cog in os.listdir('cogs'):
    if not cog.endswith('.py'):
        continue
    try:
        bot.load_extension(f'cogs.{cog[:-3]}')
    except (SyntaxError, ImportError) as e:
        print(f'Failed to load {cog}: {type(e).__name__}: {e}')

    @bot.event
    async def on_message(message):
        if not bot.is_ready() or message.author.bot:
            return

        await bot.process_commands(message)

    @bot.event
    async def on_ready():
        print('Login successful.')
        print(f'Logged in as: {bot.user.name}')
        print(f'Bot ID: {bot.user.id}')
        print(f'Server count: {len(bot.guilds)}')

bot.run(config['token'])
