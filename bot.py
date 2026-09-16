import discord
from discord.ext import commands
from config import PREFIX,TOKEN
from comandos import *
from datetime import datetime

bot = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all())

bot.inicio = datetime.now()

@bot.event
async def setup_hook():
    await bot.load_extension("comandos.Diversão.ola")
    await bot.load_extension("comandos.Utilitários.ajuda")
    await bot.load_extension("comandos.Diversão.pergunta")
    await bot.load_extension("comandos.Utilitários.info")
    await bot.load_extension("comandos.Utilitários.uptime")
    await bot.load_extension("eventos.mention")



@bot.event
async def on_message(message):
    if message.author == bot.user:
        return 

    mensagem = message.content.lower()
    autor = message.author
    servidor = message.guild
    canal = message.channel
    
    if not mensagem.startswith(PREFIX):
        print("Mensagem ignorada: sem prefixo.")
        return

    print(f"\nMessage Log:")
    print(f" > Autor: {autor}")
    print(f" > Conteúdo: {mensagem}")
    print(f" > Servidor: {servidor}")
    print(f" > Canal: {canal}\n")

    await bot.process_commands(message)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.reply("Esse comando não existe!")
bot.run(TOKEN)