from discord.ext import commands
from discord.ext.commands import Context
import aiohttp


class Bb(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()

    @commands.command()
    @commands.is_nsfw()  # Check to ensure the channel is marked NSFW.
    async def boobs(self, ctx):
        """ Pictures of boobs. """
        await self.send_bb_image('boobs')
        # Sends an image of boobs to the current channel.

    @commands.command()
    @commands.is_nsfw()  # Check to ensure the channel is marked NSFW.
    async def ass(self, ctx):
        """ Pictures of ass. """
        await self.send_bb_image(ctx, 'ass')
        # Sends an ass image to the current channel.

    @commands.command()
    async def cat(self, ctx):
        """ Cats. """
        await self.send_neko_image(ctx, 'meow')
        # Sends an image from the "meow" category to the current channel

    @commands.command()
    @commands.is_nsfw()  # Check to ensure the channel is marked NSFW.
    async def lewdn(self, ctx):
        """ Lewd nekos. """
        await self.send_neko_image(ctx, 'lewd')
        # Sends an image from the "lewd" category to the current channel

    async def send_bb_image(self, ctx: Context, category: str):
        async with self.session.get(f'https://boob.bot/api/v2/img/{category}',  # "async with" allows the response to be closed automatically
                                    headers={'key': self.bot.config['key']}) as resp:  # once this block is exited, to ensure resources are freed.
            if resp.status != 200:
                await ctx.send('The API responded with a non-200 code.')

            json = await resp.json()  # Converts the response body into a JSON object.
            await ctx.send(json['url'])

    async def send_neko_image(self, ctx: Context, category: str):
        async with self.session.get(f'https://nekos.life/api/v2/img/{category}') as resp:
            # "async with" allows the response to be closed automatically upon exiting this block
            # which ensures resources are freed.
            if resp.status != 200:
                await ctx.send('The API responded with a non-200 code.')

            json = await resp.json()  # Converts the response body into a JSON object.
            await ctx.send(json['url'])


def setup(bot):
    bot.add_cog(Bb(bot))
