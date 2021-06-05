import discord
import os
import random
import randfacts
import bibi

client = discord.Client()

x = randfacts.getFact()



@client.event


async def on_ready():
  print('{0.user} has been logged.'.format(client))

@client.event
async def on_message(recievedMessage):
  if recievedMessage.author == client.user:
    return

  if recievedMessage.author.id == ('506066994315919360'):
        choicesa = ('no', 'shutup', 'youre wasting my time', 'K.', 'oh god its you', '....' , 'dude go away' , 'WHAT DO YOU WANT' , 'nah' , 'i dont talk to gay people')
        await recievedMessage.channel.send(random.choice(choicesa))


  if recievedMessage.content.startswith('i\'d fuck the shit out of her'):
    await recievedMessage.channel.send('same bro')





  if recievedMessage.content.startswith('>fact'):
    await recievedMessage.channel.send(x)
print(x)
client.run(os.environ['TOKEN'])
