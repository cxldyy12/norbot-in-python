from discord.ext import commands
import discord
from utils import get_uptime

class uptime (commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(
        name="uptime",
        help="Responde com o tempo da atividade",
        extras={'categoria': 'Utilitários'}
    )
    async def uptime(self, message):

        embed1 = discord.Embed(
            title="Uptime",
            description=get_uptime(self.bot),
            color=discord.Color.yellow()
        )

        await message.channel.send(embed = embed1)

async def setup(bot):
    await bot.add_cog(uptime(bot))