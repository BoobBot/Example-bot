import discord
from discord.ext import commands
import aiohttp
import json



class Bb(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()
        self.color = 0x8A2BE2


    @commands.command()
    async def boobs(self, ctx):
        """Boobs"""
        ch = ctx.channel
        if ch.is_nsfw():
            page = await self.session.get("https://boob.bot/api/v2/img/boobs", headers={"key": self.bot.config["key"]})
            resp = await page.json()
            em = discord.Embed(colour=self.color)
            em.set_image(url=resp["url"])
            await ctx.send(embed=em)
        else:
            await ctx.send("This can only be ran in a NSFW channel.")
        

    @commands.command()
    async def ass(self, ctx):
        """Booty"""
        ch = ctx.channel
        if ch.is_nsfw():
            page = await self.session.get("https://boob.bot/api/v2/img/ass", headers={"key": self.bot.config["key"]})
            resp = await page.json()
            em = discord.Embed(colour=self.color)
            em.set_image(url=resp["url"])
            await ctx.send(embed=em)
        else:
            await ctx.send("This can only be ran in a NSFW channel.")

    @commands.command()
    async def cat(self, ctx):
        """Cats"""
        page = await self.session.get("https://nekos.life/api/v2/img/meow")
        resp = await page.json()
        em = discord.Embed(colour=self.color)
        em.set_image(url=resp["url"])
        await ctx.send(embed=em)

    @commands.command()
    async def lewdn(self, ctx):
        """Lewd nekos"""
        ch = ctx.channel
        if ch.is_nsfw():
            page = await self.session.get("https://nekos.life/api/v2/img/lewd")
            resp = await page.json()
            em = discord.Embed(colour=self.color)
            em.set_image(url=resp["url"])
            await ctx.send(embed=em)
        else:
            await ctx.send("This can only be run in a NSFW channel.")


def setup(bot):
    bot.add_cog(Bb(bot))
