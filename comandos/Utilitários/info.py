from discord.ext import commands
import discord
from config import PREFIX
from utils import get_uptime

class botinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="botinfo",
        help="Responde com informações do bot",
        extras={'categoria': 'Utilitários'}
    )
    async def botinfo(self, ctx):
        embed1 = discord.Embed(
            title="MINHAS INFORMAÇÕES :information_source:",
            description="Fui criado por <@1168963270170923091>",
            color=discord.Color.dark_purple()
        )

        servidores = len(self.bot.guilds)
        ping = round(self.bot.latency * 1000)
        name = self.bot.user.name

        embed1.add_field(
            name = "Meu nome é ",
            value= f'{name}', 
            inline= False)
        
        embed1.add_field(
            name = "Estou em",
            value= f'{servidores} servidores', 
            inline= False)
        
        embed1.add_field(
            name = "Meu ping atual:",
            value= f'{ping}')
        
        uptime = get_uptime(self.bot)

        embed1.add_field(
            name="Online há",
            value=uptime,
            inline=False)

        embed1.add_field(
            name = "Biblioteca:",
            value= f"Discord.py v2.7.1", 
            inline=False)
        
        embed1.add_field(
            name = "Linguagem",
            value= f"Python")

        embed1.add_field(
            name = "Lista de Comandos:",
            value= f"`{PREFIX}ajuda`", 
            inline=False)

        await ctx.reply(embed = embed1)
        
async def setup(bot):
    await bot.add_cog(botinfo(bot))


