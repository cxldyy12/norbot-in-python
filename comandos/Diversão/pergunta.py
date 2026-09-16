from discord.ext import commands
import random

class pergunta(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(
        name ="pergunta",
        description = "Faça uma pergunta e receba uma resposta aleatória",
        extras = {'categoria': 'Diversão'}
    )
    async def pergunta(self, ctx):
        respostas = ["Sim!", "Talvez...", "Não.", "Eu não sei..."]
        num = random.choice(respostas)

        await ctx.reply(num)


async def setup(bot):
    await bot.add_cog(pergunta(bot))