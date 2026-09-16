from discord.ext import commands
import discord
import math
from datetime import datetime

class uptime (commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(
        name="uptime",
        help="Responde com o tempo da atividade",
        extras={'categoria': 'Utilitários'}
    )
    async def uptime(self, message):

        uptim = datetime.now() - self.bot.inicio
        totalSeconds = math.floor(uptim / 1000)
        days = math.floor(totalSeconds / 86400)
        hours = math.floor((totalSeconds % 86400) / 3600)
        minutes = math.floor((totalSeconds % 3600) / 60)
        seconds = totalSeconds % 60
        uptime = f'${days} dias, ${hours} horas, ${minutes} minutos e ${seconds} segundos'

        embed1 = discord.Embed(
            title="Uptime",
            description=f'{uptime}',
            color=discord.Color.green()
        )

        await message.channel.send(embed = embed1)

async def setup(bot):
    await bot.add_cog(uptime(bot))