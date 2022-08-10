import discord
from discord.ext import commands
import random

Bot = commands.Bot("")

@Bot.event
async def on_ready():
    print("KaChow")


@Bot.command()
async def şimşek(ctx, sence):

    random_answer = [('sanmam'),
                     ('evet'),
                     ('hayır'),
                     ('bilemiyorum'),
                     ('hahaaha mümkün değil'),
                     ('kesinlikle')]
    await ctx.send(random.choice(random_answer))

@Bot.command()
async def nedinlemeliyim(ctx):
    random_song = [('https://open.spotify.com/track/0JUaqijY6i3hBzOdHGMP9j?si=WArDkcUdROefC1A_vM--Qg'),
                         ('https://open.spotify.com/track/45KlnSuaOM4ypW2FTQCu2Z?si=F0KAdUC2Sk6ujD2Y46Fb3A'),
                         ('https://open.spotify.com/track/02SjT88MukDOa9KuuRuODY?si=483AKzElSrmMjDTcPlkUIg'),
                         ('https://open.spotify.com/track/26HE8ehnFL86hkL6JCn9gY?si=8nq9pxdlQJSFpYv6ltJDdQ'),
                         ('https://open.spotify.com/track/1ENnpCRfGWQLVGL9pEyVao?si=hxzfDsU_TCGtQXQOnhW8xg'),
                         ('https://open.spotify.com/track/3O0kOIdSdb3xQnjoi1AjRD?si=ZITiwgvkRBKSozGite1cHw'),
                         ('https://open.spotify.com/track/6YpU93CdpOUWGThYgcC7jp?si=cfoRXzETQkK9xcua9evncg'),
                         ('https://open.spotify.com/track/3rUBFGjLPvEAWR1LlJcOjW?si=JbMUbdLuSKyAydztpBe7rA'),
                         ('https://open.spotify.com/track/3VQOzC6hxDgZXgOWBGoAoV?si=4qPvAsGwRdunUhkKgxuHYA'),
                         ('https://open.spotify.com/track/0lJ4PT7e4nmtZJIoElhPlD?si=iUds4D28Qh2tBsWS_0_dig')]
    await ctx.send(random.choice(random_song))

@Bot.command()
async def Cadillac(msg, gibi, uç):
    await msg.send('BMW gibi sok')

@Bot.command()
async def nasılsın(msg, şimşek):
    await msg.send('hız, ben hızım')

@Bot.command()
async def iyi(msg, geceler):
    await msg.send('İyi geceler. KaChow')

@Bot.command()
async def Evlat(msg, az, önce, piston, kupasını, kaybettin, farkında, mısın):
    await msg.send('Ahh, tanıdığım mızmız, yaşlı bir yarış arabası bana şöyle demişti: Kupa dediğin boş bir kasedir..')

@Bot.command()
async def günaydın(msg):
    await msg.send('günaydın canım')


@Bot.command()
async def McQueen(msg):
    await msg.send('Ka-Ch<ow!')

@Bot.command()
async def nasıl(msg):
    await msg.send('fazla bile adamsın')

Bot.run("x") //bot token for x