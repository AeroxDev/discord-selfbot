from discord.ext import commands
import time
import random

bot = commands.Bot(">>>", self_bot=True) #u can change the prefix from >>> to anything u want 
klist = ['wsell all','wbattle','whunt'] 
token=input('Token : ')

@bot.event
async def on_ready():
    print("Bot presence t u r n e d on ( ͡° ͜ʖ ͡°)")

@bot.command()
async def test(ctx):
    while True:
        import random
        n = random.randint(20,59) #cooldown
        k = random.choice(klist)
        print(k) #print command
        print(n)
        time.sleep(n)
        await ctx.send(k)

bot.run(token, bot=False)
