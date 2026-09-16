from discord.ext import commands

class ola(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="ola",
        help="Responde com uma mensagem de saudação.",
        extras={'categoria': 'Utilitários'}
    )
    async def ola(self, ctx):
        if ctx.author != self.bot.user:
            await ctx.send("Olá! Como posso ajudar você hoje?")

async def setup(bot):
    await bot.add_cog(ola(bot))