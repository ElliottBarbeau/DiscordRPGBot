import discord
from Player import Player

client = discord.Client()
users = []
players = []
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #Real bot code here
    if message.content.startswith('!'):
        if "startadventure" in message.content.lower() and message.author.id not in users:
            await message.channel.send("\n```yaml\n============================================================\nYour adventure has begun!\n============================================================\nTo choose a class, type one of the following commands:\n"
                + "\n!mage \n!knight \n!rogue \n!archer\n\n============================================================\n```".format(message))
            
        elif "mage" in message.content.lower() and message.author.id not in users:
            players.append(Player('mage', message.author))
            users.append(message.author.id)
            await send_embark('mage', message)
            
        elif "knight" in message.content.lower() and message.author.id not in users:
            players.append(Player('knight', message.author))
            users.append(message.author.id)
            await send_embark('knight', message)
            
        elif "rogue" in message.content.lower() and message.author.id not in users:
            players.append(Player('rogue', message.author))
            users.append(message.author.id)
            await send_embark('rogue', message)
            
        elif "archer" in message.content.lower() and message.author.id not in users:
            players.append(Player('archer', message.author))
            users.append(message.author.id)
            await send_embark('archer', message)
            
        if "profile" in message.content.lower():
            await message.channel.send(players[users.index(message.author.id)].print_profile(message.author.name))
            
        elif "skills" in message.content.lower():
            await message.channel.send(players[users.index(message.author.id)].print_skills(message.author.name))
            
        if "upgrade" in message.content.lower():
            if ("strength" in message.content.lower()):
                skill = "strength"
                for integer in message.content.lower().split():
                    try: 
                        int(integer)
                        await message.channel.send(players[users.index(message.author.id)].add_points(skill, integer))
                    except ValueError:
                        continue
            elif ("dexterity" in message.content.lower()):
                skill = "dexterity"
                for integer in message.content.lower().split():
                    try: 
                        int(integer)
                        await message.channel.send(players[users.index(message.author.id)].add_points(skill, integer))
                    except ValueError:
                        continue
            elif ("agility" in message.content.lower()):
                skill = "agility"
                for integer in message.content.lower().split():
                    try: 
                        int(integer)
                        await message.channel.send(players[users.index(message.author.id)].add_points(skill, integer))
                    except ValueError:
                        continue
            elif ("magic" in message.content.lower()):
                skill = "magic"
                for integer in message.content.lower().split():
                    try: 
                        int(integer)
                        await message.channel.send(players[users.index(message.author.id)].add_points(skill, integer))
                    except ValueError:
                        continue

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------------------')

async def send_embark(player_class, message):
    await message.channel.send("\n```yaml\nCongratulations! You have will embark on your journey as a " + player_class + "!\n```")

client.run('NTM2MDA4MTQwODAyNjIxNDQy.DyQcWA.nMhtnyH0KeNbD1__us6OQaULsQo')
