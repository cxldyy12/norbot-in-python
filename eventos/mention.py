from discord.ext import commands
import discord
from config import PREFIX

class mention(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        autor = message.author
        
        embed = discord.Embed(
            title=f'Olá {autor}! Eu sou o NorBot',
            description="Para ver a lista de comandos disponíveis, digite `$ajuda`.",
            color=discord.Color.purple(),
            )
        if message.content == "<@767556586695819266>":
            await message.channel.send(embed = embed)

async def setup(bot):
    await bot.add_cog(mention(bot))