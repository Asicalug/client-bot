import discord
from discord import ui
from discord import Interaction
from discord.ext import commands



CreateSuggestionEmbed = discord.Embed(title="Suggestion", description="Create a Suggestion here")
CreateSuggestionButton = discord.ui.Button(label="Create Suggestion", style=discord.ButtonStyle.blurple)

intents = discord.Intents().all()
client = commands.Bot(command_prefix = ('.'), intents=intents)
client.remove_command('help')


#===classes===
class Hi(ui.Modal, title='Questionnaire Response'):
    name = ui.TextInput(label='Name')
    answer = ui.TextInput(label='Answer', style=discord.TextInputStyle.paragraph)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Thanks for your response, {self.name}!', ephemeral=True)

class CreateTicket(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="Create Suggestion", style=discord.ButtonStyle.grey)
    async def createsugg(self, button: discord.ui.button, interaction: Interaction):
        user = interaction.user
        await interaction.response.send_modal(modal=Hi())


#===commands===
@client.slash_command(name="setupsugg", description="Creates a Message to setup suggestions")
async def setupsugg(interaction : discord.Interaction):
    view = CreateTicket()
    await interaction.response.send_message("Suggestion Creator has been setup", ephemeral=True)
    await interaction.channel.send(embed=CreateSuggestionEmbed, view=view) 


client.run('MTEwNDIxODc5NjE5OTI1NjE4Ng.GpeKl0.3XjqTAqy6xYAliHT-CbHPmFxReJpdN9B5xPxEU')