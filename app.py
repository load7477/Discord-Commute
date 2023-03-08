import discord
import warnings, aiohttp, re
from discord.ui import InputText, Modal
from discord.commands import Option
from discord.ui import Button, View, Select

intents = discord.Intents.all()
client = discord.Bot(intents=intents, debug_guilds=[985258143447662622])

adminli = []

@client.event
async def on_ready():
    channel = client.get_channel(1081679993786085406)
    main_view = View()
    main_view.add_item(Button(label="확인하기", style=discord.ButtonStyle.primary, custom_id="view"))
    main_view.stop()
    msgs = await channel.send("@everyone",embed=discord.Embed(color=0x5865F2, title="출퇴근", description="출퇴근 시스템"), view=main_view)

@client.event
async def on_message(message):
    if message.content == '!setting':
        await message.delete()
        main_view = View()
        main_view.add_item(Button(label="출근", style=discord.ButtonStyle.primary, custom_id="on"))
        main_view.add_item(Button(label="퇴근", style=discord.ButtonStyle.primary, custom_id="off"))
        main_view.stop()
        await message.channel.send("", view=main_view)

@client.listen("on_interaction")
async def on_interaction(interaction):
    if not interaction.is_component():
        return
    if not interaction.data["component_type"] == 2:
        return
    custom_id = interaction.data["custom_id"]
    
    if custom_id == "on":
        print(adminli)
        print()
        if interaction.user.name in adminli:
            await interaction.response.send_message(
                f"이미 출근중입니다", ephemeral=True
            )
        else:
            await interaction.response.send_message(
                f"출근 완료", ephemeral=True
            )
            adminli.append(interaction.user.name)
    elif custom_id == "off":
        if interaction.user.name in adminli:
            await interaction.response.send_message(
                f"퇴근 완료", ephemeral=True
            )
            adminli.remove(interaction.user.name)
        else:
            await interaction.response.send_message(
                f"출근중이 아닙니다", ephemeral=True
            )

    elif custom_id == "view":
        print(adminli)
        if adminli == '[]':
            await interaction.response.send_message(
                f"출근중인 어드민이 없습니다", ephemeral=True
            )
        else:
            for n in adminli:
                await interaction.response.send_message(
                    f"출근중인 어드민 : {n} \n", ephemeral=True
                )

client.run("MTA4MTY3NTE5MTYxNDE4OTcxOA.G-yR65.6wbGbLN3S_ntBYYeTrFSEB6deJJWLA9TmQFImo")