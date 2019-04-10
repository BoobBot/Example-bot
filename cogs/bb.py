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

    @commands.command()
    @commands.is_nsfw()  # Check to ensure the channel is marked NSFW.
    async def ass(self, ctx):
        """ Pictures of ass. """
        await self.send_bb_image(ctx, 'ass')

    @commands.command()
    async def cat(self, ctx):
        """ Cats. """
        await self.send_neko_image(ctx, 'meow')

    @commands.command()
    @commands.is_nsfw()  # Check to ensure the channel is marked NSFW.
    async def lewdn(self, ctx):
        """ Lewd nekos. """
        await self.send_neko_image(ctx, 'lewd')

    async def send_bb_image(self, ctx: Context, category: str):
        """
        Makes a request to BoobBot's API for an image in the given category.
        If the request is successful, the URL is extracted from the response JSON
        and sent to `ctx.channel`.
        """
        async with self.session.get(f'https://boob.bot/api/v2/img/{category}',
                                    headers={'key': self.bot.config['key']}) as resp:
            # An "async with" block allows "resp" to be automatically closed once this block is exited.
            # This means that resources, such as threads and memory, can be freed up for later re-use.
            if resp.status != 200:
                await ctx.send('The API responded with a non-200 code.')

            json = await resp.json()
            await ctx.send(json['url'])

    async def send_neko_image(self, ctx: Context, category: str):
        """
        Makes a request to neko.life's API for an image in the given category.
        If the request is successful, the URL is extracted from the response JSON
        and sent to `ctx.channel`.
        """
        async with self.session.get(f'https://nekos.life/api/v2/img/{category}') as resp:
            # An "async with" block allows "resp" to be automatically closed once this block is exited.
            # This means that resources, such as threads and memory, can be freed up for later re-use.
            if resp.status != 200:
                await ctx.send('The API responded with a non-200 code.')

            json = await resp.json()
            await ctx.send(json['url'])


def setup(bot):
    bot.add_cog(Bb(bot))
