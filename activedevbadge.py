import discord
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s): {[cmd.name for cmd in synced]}")
    except Exception as e:
        print(f"Error syncing commands: {e}")

@bot.tree.command(name="activedeveloperbadge", description="Claim your Active Developer Badge.")
async def activedeveloperbadge(interaction: discord.Interaction):
    await interaction.response.send_message(
        "🎉 Success! This counts toward your Active Developer Badge.\n\n"
        "📌 To claim your **Active Developer Badge**, visit:\n"
        "👉 https://discord.com/developers/active-developer\n"
        "🕒 Check back in ~24 hours to claim it. You only need to do this once.",
        ephemeral=True
    )

bot.run("YOUR-BOT-TOKEN-HERE")
