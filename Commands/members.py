import discord
from discord import app_commands, SelectOption, Interaction
from discord.ext import commands, tasks
from discord.ui import Button, View, Select
import re


class MembersCommand(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @app_commands.command(name="help", description="Shows the help menu")
    async def help(self, interaction : Interaction):
        try:
            view = mView()
            await interaction.response.send_message("Help menu", view=view)
        except Exception as e:
            print(e)

class mView(View):
    def __init__(self):
        try:
            super().__init__(timeout=None)
            b = Button(label="Click here", style=discord.ButtonStyle.primary, custom_id="help")
            async def callbackt(interaction):
                await interaction.response.send_message("Help menu")
            b.callback = callbackt
            self.add_item(b)
        except Exception as e:
            print(e)
    
    
    

async def setup(client):
    await client.add_cog(MembersCommand(client))