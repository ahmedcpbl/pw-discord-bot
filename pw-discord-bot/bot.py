import discord
from discord.ext import commands

TOKEN = "NTM2NTM0MzE5OTM0NjAzMjY1.DyYGDA.VujZpgHb8Ach2NbnFSgwd1mTMKY"
ADMIN = "Pøkemon"

client = commands.Bot(command_prefix='/')

@client.event
async def on_ready():
	print("The bot is ready!")
	admin = discord.utils.get(client.get_all_members(), name=ADMIN)
	print("The admin is: " + str(admin))
	await client.change_presence(game=discord.Game(name="Dofus"))
	await client.send_message(admin, "Le Bot est Pret")

questions = [
	'Nom du Perso',
	'Ton niveau',
	'Motivation',
]

data = dict()

@client.event
async def on_message(message):
	channel = message.channel
	if message.author == client.user:
		return
	if message.content == "/apply":
		if channel.is_private:
			return
		else:
			data[message.author] = {
				'step' : 0
			}
			await client.send_message(message.author, questions[data[message.author]['step']])
			data[message.author]['step'] += 1
	if channel.is_private:
		if data[message.author]['step'] > len(questions):
			return		
		if data[message.author]['step'] == 1:
			data[message.author]['Nom du Perso'] = message.content
		if data[message.author]['step'] == 2:
			data[message.author]['Niveau'] = message.content
		if data[message.author]['step'] == 3:
			data[message.author]['Motivation'] = message.content

		if data[message.author]['step'] == len(questions):
			admin = discord.utils.get(client.get_all_members(), name=ADMIN)
			await client.send_message(admin, "Nouvelle Candidature")
			await client.send_message(admin, "Nom du Perso: " +  data[message.author]['Nom du Perso'])
			await client.send_message(admin, "Niveau: " +  data[message.author]['Niveau'])
			await client.send_message(admin, "Motivation: " +  data[message.author]['Motivation'])
			data[message.author]['step'] += 1
			return
		await client.send_message(message.author, questions[data[message.author]['step']])
		data[message.author]['step'] += 1

client.run(TOKEN)