from discord.ext import commands
import time
import random

bot = commands.Bot(">>>", self_bot=True)
klist = ['wsell all','wbattle','whunt']
token=input('Token : ')

@bot.event
async def on_ready():
    print("Bot presence t u r n e d on ( ͡° ͜ʖ ͡°)")

@bot.command()
async def test(ctx):
    while True:
        import random
        n = random.randint(20,59)
        k = random.choice(klist)
        print(k)
        print(n)
        time.sleep(n)
        await ctx.send(k)

bot.run(token, bot=False)
