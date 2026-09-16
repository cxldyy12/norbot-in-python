from discord.ext import commands
import discord
from config import PREFIX

class ajuda(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name = "ajuda",
        help = "Exibe a lista de comandos disponíveis.",
        extras = {'categoria': 'Utilitários'}
    )
    async def ajuda(self, ctx):
        embed = discord.Embed(
            title="AJUDA",
            description=f'Olá {ctx.author.mention}! Aqui estão os comandos disponíveis:',
            color=discord.Color.blue()
        )
        embed.set_footer(text=f'Prefixo: {PREFIX}')

        for comando in self.bot.commands:
            categoria = comando.extras.get("categoria", "Administração, Diversão, Sets, Utilitários")
            texto = f'`${comando.name}` — {comando.help}'

            embed.add_field(
                name = categoria,
                value=texto, 
                inline=False)
        
        await ctx.reply(embed = embed)

async def setup(bot):
    await bot.add_cog(ajuda(bot))