from datetime import datetime

def get_uptime(bot):
    totalSeconds = int((datetime.now() - bot.inicio).total_seconds())

    days = totalSeconds // 86400
    hours = (totalSeconds % 86400) // 3600
    minutes = (totalSeconds % 3600) // 60
    seconds = totalSeconds % 60

    return f"{days} dias, {hours} horas, {minutes} minutos e {seconds} segundos"