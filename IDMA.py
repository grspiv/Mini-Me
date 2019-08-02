import discord
from discord.ext import commands, tasks
from itertools import cycle
import random
def read_token():
    with open("./config/token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()
token = read_token()

bot = commands.Bot(command_prefix='-')
status = cycle(['Firefly', 'D&D', 'Monopoly', 'Stranger Things', 'Star Wars', 'Zelda', 'Pacman', 'Motral Kombat', 'Life', 'with my emotions', 'with myself', 'Nothing', "I'm bored"])
@tasks.loop(seconds=60)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))

@bot.event
async def on_ready():
    change_status.start()
    print("It's aliiiiiive!!!!")
    await bot.change_presence(activity=discord.Game(name='with code'))


@bot.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    ''': Ask a question and I shall shake my magic 8 ball for you!'''
    responses = ['It is certain.',
                 'It is decidedly so.',
                 'Without a doubt.',
                 'Yes - definitely.',
                 'You may rely on it.',
                 'As I see it, yes.',
                 'Most likely.'
                 'Outlook good.',
                 'Yes.',
                 'Signs point to yes.',
                 'Reply hazy, try again.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 "Don't count on it.",
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Very doubtful.']

    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
    user = ctx.author
    channel = ctx.channel
    guild = ctx.guild
    print(guild, '.', channel, '.', user, ' - 8ball')


bot.run(token)
