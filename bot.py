import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import time

bot = commands.Bot(command_prefix = ('!', '.'), case_insensitive = True)
TOKEN = 'token'
game = discord.Game(name = 'game name')
compliments = ["Y- You're really sweet.",
"You're doing great!",
"11/10 you're rocking it!",
'You are simply amazing.',
'You are the most perfect you there is.',
'I believe in you.',
"You... you're so cool!",
'I love you as much as I love potatoes. A lot.',
'You are one of a kind.',
"It's not easy to be me... which is why I need you.",
'Are you a beaver, because *damn*',
'What an amazing person, honestly.',
'What a cutie...',
'I.. I appreciate you!',
'On a scale of one to fabulous you are killing it.',
'I only give compliments to the best people in the world. Guess what that makes you?',
'You are a gift to this world.',
'I bet you sweat glitter. :sparkles:',
"Help, I've fallen for you and I don't want to get up",
"All I want to do is Taco 'bout you\nhttps://imgur.com/RLqDheY",
'You are un-boo-lieveable \nhttps://imgur.com/aVIBb6M',
'https://imgur.com/a6m4CK2',
'You are one in a melon! :watermelon: \nhttps://imgur.com/bBRJ0ec',
'Whale whale whale :whale: \nLooks like someone (you) is being totally awesome! \nhttps://imgur.com/kcRTU1T',
':dizzy: You leave me *star*struck :dizzy:',
'I love you *beary* much. \nhttps://imgur.com/ux97dTB',
'If you were a fruit you would be a fine-apple \nhttps://imgur.com/RxfoRAR',
'I have as much love for you as Luc has for Xolia.',
'You are wonderful, just believe in yourself.',
'If it looks like I don\'t like you, it\'s only because I\'m mad at myself for not loving you enough.'
]

@bot.event
async def on_ready():
    await bot.change_presence(activity = game)
    print("Bot is online and connected to Discord")

#start of commands
@bot.command()
async def ping():
    await bot.say('pong!')

@bot.command()
async def rps(item):
    item = item.lower()
    if (item == 'rock' or item == 'paper' or item == 'scissors'):
        rpsChoices = ['rock', 'paper', 'scissors']
        botChoice = random.choice(rpsChoices)
        #rock
        if item == 'rock':
            if botChoice == 'rock':
                bot.say('I chose rock. It\'s a tie!')
            elif botChoice == 'paper':
                bot.say('I chose paper. Paper beats rock. I win!')
            elif botChoice == 'scissors':
                bot.say('I chose scissors. Rock beats scissors. You win!')
        #paper
        elif item == 'paper':
            if botChoice == 'rock':
                bot.say('I chose rock. Paper beats rock. You win!')
            elif botChoice == 'paper':
                bot.say('I chose paper. It\'s a tie!')
            elif botChoice == 'scissors':
                bot.say('I chose scissors. Scissors beats paper. I win!')
        #scissors
        elif item == 'scissors':
            if botChoice == 'rock':
                bot.say('I chose rock. Rock beats scissors. I win!')
            elif botChoice == 'paper':
                bot.say('I chose paper. Scissors beats paper. You win!')
            elif botChoice == 'scissors':
                bot.say('I chose scissors. It\'s a tie!')
    else:
        bot.say('That is not a valid choice.')


@bot.command(pass_context=True)
async def say(ctx, *, args):
    await bot.say(args)
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def uwu(ctx, *, args):
	await bot.delete_message(ctx.message)
	await bot.say(args + ' uwu')

@bot.command()
async def snap():
    await bot.say('https://imgur.com/GbgE5OE')

@bot.command()
async def smile():
    await bot.say('https://imgur.com/1Iwlo7L')

@bot.command()
async def fish():
    fishes = ['https://imgur.com/7isI1D4',
    'https://imgur.com/w7cyWHP', 'https://imgur.com/s0nQhGH',
    'https://imgur.com/hExgMRH', 'https://imgur.com/EgKyrNN',
    'https://imgur.com/HT7EinZ', 'https://imgur.com/gxXamHR',
    'https://imgur.com/W1xivYe', 'https://imgur.com/E5Hl1Ee']
    await bot.say(random.choice(fishes))

@bot.command()
async def thicc():
    await bot.say('https://imgur.com/yh1UUiF')

@bot.command()
async def compliment():
    nice = random.choice(compliments)
    await bot.say(nice)

bot.run(TOKEN)
